import os
import re
import sys
import warnings
import pdfplumber
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

# =====================================================
# INTERFACE DE ENTRADA/SAÍDA INTERATIVA
# =====================================================
print("\n=======================================================")
print("   SISTEMA INTEGRADO DE EXTRAÇÃO DE FATURAS - v3.8")
print("=======================================================")
PASTA_ENTRADA = input("Digite ou cole a pasta de ENTRADA (PDFs/CSVs): ").strip()
PASTA_SAIDA   = input("Digite ou cole a pasta de SAÍDA (Excel): ").strip()
print("=======================================================\n")

PASTA_ENTRADA = PASTA_ENTRADA.replace('"', '')
PASTA_SAIDA = PASTA_SAIDA.replace('"', '')

if not os.path.exists(PASTA_ENTRADA):
    print(f"❌ Erro: A pasta de entrada '{PASTA_ENTRADA}' não existe.")
    sys.exit()
os.makedirs(PASTA_SAIDA, exist_ok=True)

MESES_MAP = {
    'JAN': '01', 'FEV': '02', 'MAR': '03', 'ABR': '04', 'MAI': '05', 'JUN': '06',
    'JUL': '07', 'AGO': '08', 'SET': '09', 'OUT': '10', 'NOV': '11', 'DEZ': '12'
}

# =====================================================
# FUNÇÕES AUXILIARES DE LIMPEZA E TRATAMENTO
# =====================================================

def limpar_valor(valor_str):
    if not valor_str: return 0.0
    if isinstance(valor_str, (int, float)): return float(valor_str)
    valor_str = valor_str.replace('.', '').replace(',', '.')
    try: return float(valor_str)
    except ValueError: return 0.0

def formatar_moeda_texto(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def calcular_data_original_compra(dia_str, mes_str, ano_fatura, mes_fatura, p_atual):
    """
    Inteligência Temporal Suprema (v3.8):
    Calcula a data real em que a compra foi feita baseada no histórico de parcelas,
    evitando erros em compras longas (ex: 24 parcelas feitas em 2024 aparecendo em 2026).
    """
    dia_compra = int(dia_str)
    mes_compra = int(mes_str)
    
    # 1. Cria uma data base usando o ano da fatura e o mês impresso na linha da compra
    # Se a fatura é de Jan/Fev e a linha diz Dez, ajustamos temporariamente o ano base para trás
    ano_base = ano_fatura
    if mes_fatura in [1, 2] and mes_compra in [11, 12]:
        ano_base = ano_fatura - 1
        
    data_referencia_linha = datetime(ano_base, mes_compra, dia_compra)
    
    # 2. Aplica a máquina do tempo baseada na parcela atual
    # Se for parcela 15, precisamos voltar 14 meses no passado para achar o dia da compra original
    meses_a_subtrair = p_atual - 1
    
    if meses_a_subtrair > 0:
        data_original = data_referencia_linha - relativedelta(months=meses_a_subtrair)
    else:
        data_original = data_referencia_linha
        
    return data_original.strftime('%Y-%m-%d')

# =====================================================
# MOTORES SANTANDER
# =====================================================

def buscar_total_santander(pdf_path):
    padrao_valor_puro = re.compile(r'([\d\.]+,\d{2})')
    padrao_saldo_fatura = re.compile(r'Saldo Desta Fatura\s+([\d\.]+,\d{2})', re.IGNORECASE)
    with pdfplumber.open(pdf_path) as pdf:
        texto_p1 = pdf.pages[0].extract_text()
        if texto_p1:
            linhas = [l.strip() for l in texto_p1.split('\n') if l.strip()]
            for i, linha in enumerate(linhas):
                if "VALOR DESTA FATURA" in linha.upper():
                    for j in range(1, 3):
                        if i + j < len(linhas):
                            match = padrao_valor_puro.search(linhas[i + j])
                            if match: return limpar_valor(match.group(1))
        if len(pdf.pages) >= 4:
            texto_p4 = pdf.pages[3].extract_text()
            if texto_p4:
                match_resumo = padrao_saldo_fatura.search(texto_p4)
                if match_resumo: return limpar_valor(match_resumo.group(1))
    return 0.0

def extrair_taxas_santander(pdf_path):
    rotativo, mora, multa = "Não localizado", "Não localizado", "Não localizado"
    regex_rotativo = re.compile(r'crédito\s+rotativo:\s*juros:\s*([\d\.]+,\d{2}\s*%\s*a\.m\.)', re.IGNORECASE)
    regex_mora     = re.compile(r'juros\s+moratórios:\s*([\d\.]+,\d{2}\s*%\s*a\.m\.)', re.IGNORECASE)
    regex_multa    = re.compile(r'multa\s+de\s*([\d\.]+,\d{2}\s*%)', re.IGNORECASE)
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_limpo = " ".join(texto.lower().split())
                if "crédito rotativo:" in texto_limpo or "juros moratórios:" in texto_limpo:
                    match_rot = regex_rotativo.search(texto_limpo)
                    match_mora = regex_mora.search(texto_limpo)
                    match_multa = regex_multa.search(texto_limpo)
                    if match_rot: rotativo = match_rot.group(1).strip()
                    if match_mora: mora = match_mora.group(1).strip()
                    if match_multa: multa = match_multa.group(1).strip()
                    break
    return f"Taxas Reais do Mês -> Rotativo: {rotativo} | Mora: {mora} | Multa: {multa}"

def processar_santander_pdf(caminho_pdf, ano_fatura, mes_fatura):
    PADRAO_SANTANDER = re.compile(r'(\d{2})/(\d{2})\s+(.+?)(?:\s+(\d{2}/\d{2}))?\s+(-?[\d\.]+,\d{2})')
    compras = []
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if not texto: continue
            for linha in texto.split('\n'):
                linha_limpa = linha.strip()
                if not linha_limpa: continue
                linha_com_data = re.sub(r'^\d+\s+(?=\d{2}/\d{2})', '', linha_limpa)
                resultados = list(PADRAO_SANTANDER.finditer(linha_com_data))
                if resultados:
                    for match in resultados:
                        dia = match.group(1)
                        mes = match.group(2)
                        descricao = match.group(3).strip()
                        raw_parcela = match.group(4) if match.group(4) else ''
                        valor_num = limpar_valor(match.group(5))
                        
                        p_atual, p_total = 1, 1
                        if raw_parcela and '/' in raw_parcela:
                            try:
                                p_atual = int(raw_parcela.split('/')[0])
                                p_total = int(raw_parcela.split('/')[1])
                            except ValueError:
                                pass
                        
                        # Calcula a VERDADEIRA data da compra original voltando no tempo pelas parcelas
                        data_completa = calcular_data_original_compra(dia, mes, ano_fatura, mes_fatura, p_atual)
                        
                        descricao = re.sub(r'\s+\d\s+\d{2}/\d{2}.*$', '', descricao)
                        descricao = re.sub(r'\s+\d{2}/\d{2}.*$', '', descricao).strip().upper()
                        
                        if "PAGAMENTO" not in descricao and valor_num >= 0:
                            compras.append({
                                'Responsável': '', 'Banco': '', 'Período': '',
                                'Data da Compra': data_completa, 'Descrição': descricao, 
                                'Parcela Atual': p_atual, 'Parcela Total': p_total,
                                'Valor': valor_num, 'Tipo': 'Compra Corrente',
                                'Fatura Controle': 0.0, 'Memória de Cálculo': 'REGULAR'
                            })
    df = pd.DataFrame(compras).drop_duplicates(subset=['Data da Compra', 'Descrição', 'Valor']) if compras else pd.DataFrame()
    if not df.empty:
        df = df.sort_values(by=['Data da Compra'])
    return df, buscar_total_santander(caminho_pdf), extrair_taxas_santander(caminho_pdf)

# =====================================================
# MOTORES NUBANK
# =====================================================

def buscar_total_fatura_nubank(pdf_path):
    regex_total_nu = re.compile(r'Frederico\s+Amorim\s+R\$\s+([\d\.]+,\d{2})', re.IGNORECASE)
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                match = regex_total_nu.search(texto)
                if match: return limpar_valor(match.group(1))
    return 0.0

def processar_nubank_csv(caminho_csv, ano_fatura, mes_fatura):
    df_raw = pd.read_csv(caminho_csv)
    compras = []
    df_raw.columns = [c.lower().strip() for c in df_raw.columns]
    
    for _, row in df_raw.iterrows():
        try:
            dt_obj = pd.to_datetime(row['date'])
            dia = dt_obj.strftime('%d')
            mes = dt_obj.strftime('%m')
        except:
            dia, mes = "01", str(mes_fatura).zfill(2)
            
        descricao_original = str(row['title']).strip().upper()
        valor_num = limpar_valor(row['amount'])
        
        if "PAGAMENTO" not in descricao_original and "ESTORNO" not in descricao_original and valor_num >= 0:
            p_atual, p_total = 1, 1 
            descricao_limpa = descricao_original
            
            match_p = re.search(r'PARCELA\s*(\d+)/(\d+)', descricao_original)
            if match_p:
                p_atual = int(match_p.group(1))
                p_total = int(match_p.group(2))
                descricao_limpa = re.sub(r'-\s*PARCELA\s*\d+/\d+', '', descricao_original).strip()
                descricao_limpa = re.sub(r'PARCELA\s*\d+/\d+', '', descricao_limpa).strip()

            # Descobre a data primitiva baseado nas parcelas detectadas no CSV
            data_completa = calcular_data_original_compra(dia, mes, ano_fatura, mes_fatura, p_atual)

            compras.append({
                'Responsável': '', 'Banco': '', 'Período': '',
                'Data da Compra': data_completa, 'Descrição': descricao_limpa, 
                'Parcela Atual': p_atual, 'Parcela Total': p_total,
                'Valor': valor_num, 'Tipo': 'Compra Corrente',
                'Fatura Controle': 0.0, 'Memória de Cálculo': 'REGULAR'
            })
            
    df = pd.DataFrame(compras) if compras else pd.DataFrame()
    if not df.empty:
        df = df.iloc[::-1]
    return df

def processar_nubank_pdf(caminho_pdf, ano_fatura, mes_fatura):
    regex_linha_nu = re.compile(r'^(\d{2}\s+[A-Z]{3})\s+(?:••••\s+\d{4}\s+|(?:\d{2}\s+)?.*?NuPay\s+)?(.+?)\s+R\$\s+([\d\.]+,\d{2})', re.IGNORECASE)
    compras = []
    
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if not texto: continue
            for linha in texto.split('\n'):
                match = regex_linha_nu.search(linha.strip())
                if match:
                    raw_data = match.group(1).split()
                    dia = raw_data[0]
                    mes_str = raw_data[1].upper()
                    mes_num = MESES_MAP.get(mes_str, "01")
                    
                    full_descricao = match.group(2).strip().upper()
                    valor_num = limpar_valor(match.group(3))
                    
                    p_atual, p_total = 1, 1 
                    match_parcela = re.search(r'-\s*PARCELA\s*(\d+)/(\d+)', full_descricao)
                    if match_parcela:
                        p_atual = int(match_parcela.group(1))
                        p_total = int(match_parcela.group(2))
                        full_descricao = re.sub(r'-\s*PARCELA\s*\d+/\d+', '', full_descricao).strip()
                    
                    # Calcula a retroatividade temporal das parcelas do PDF
                    data_completa = calcular_data_original_compra(dia, mes_num, ano_fatura, mes_fatura, p_atual)

                    if "PAGAMENTO" not in full_descricao and "ESTORNO" not in full_descricao:
                        compras.append({
                            'Responsável': '', 'Banco': '', 'Período': '',
                            'Data da Compra': data_completa, 'Descrição': full_descricao, 
                            'Parcela Atual': p_atual, 'Parcela Total': p_total,
                            'Valor': valor_num, 'Tipo': 'Compra Corrente',
                            'Fatura Controle': 0.0, 'Memória de Cálculo': 'REGULAR'
                        })
                        
    df = pd.DataFrame(compras).drop_duplicates(subset=['Data da Compra', 'Descrição', 'Valor']) if compras else pd.DataFrame()
    return df

# =====================================================
# PROCESSAMENTO DOS ARQUIVOS EM LOTE (ORQUESTRAÇÃO)
# =====================================================

todos_arquivos = [f for f in os.listdir(PASTA_ENTRADA) if f.lower().endswith(('.pdf', '.csv'))]

if not todos_arquivos:
    print(f"ℹ️ Nenhum arquivo PDF ou CSV encontrado na pasta: {PASTA_ENTRADA}")
    sys.exit()

print(f"🔄 Encontrado(s) {len(todos_arquivos)} arquivo(s) na fila de processamento.\n")

for arquivo in todos_arquivos:
    caminho_completo = os.path.join(PASTA_ENTRADA, arquivo)
    nome_base, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()
    
    print(f"Lendo e analisando: {arquivo}...")
    
    match_data_arquivo = re.match(r'^(\d{4})-(\d{2})', arquivo)
    fora_do_padrao = False
    
    if match_data_arquivo:
        ano_fatura = int(match_data_arquivo.group(1))
        mes_fatura = int(match_data_arquivo.group(2))
        val_periodo = f"{ano_fatura}-{str(mes_fatura).zfill(2)}"
        data_fechamento_ajustada = f"{ano_fatura}-{str(mes_fatura).zfill(2)}-01"
    else:
        fora_do_padrao = True
        ano_fatura = 2026
        mes_fatura = 4
        val_periodo = "2026-04"
        data_fechamento_ajustada = "2026-04-01"
        print(f"⚠️ Alerta de Organização: O arquivo '{arquivo}' quebrou o padrão de nomes.")

    nome_maiusculo = arquivo.upper()
    if "SANTANDER" in nome_maiusculo:
        val_banco = "SANTANDER"
    elif "NUBANK" in nome_maiusculo:
        val_banco = "NUBANK"
    else:
        val_banco = "OUTRO"

    if "FRED" in nome_maiusculo:
        val_responsavel = "FRED"
    elif "LAURA" in nome_maiusculo:
        val_responsavel = "LAURA"
    elif "NOSSO" in nome_maiusculo or "CASAL" in nome_maiusculo:
        val_responsavel = "NOSSO"
    else:
        val_responsavel = "NÃO IDENTIFICADO"

    df_compras = pd.DataFrame()
    valor_total_fatura = 0.0
    resumo_taxas_mes = "Taxas do mês: Não localizado"
    
    if "SANTANDER" in arquivo.upper():
        if extensao == '.pdf':
            df_compras, valor_total_fatura, resumo_taxas_mes = processar_santander_pdf(caminho_completo, ano_fatura, mes_fatura)
        else:
            continue
            
    elif "NUBANK" in arquivo.upper():
        if extensao == '.csv':
            df_compras = processar_nubank_csv(caminho_completo, ano_fatura, mes_fatura)
            caminho_pdf_contingencia = caminho_completo.replace('.csv', '.pdf').replace('.CSV', '.pdf')
            if os.path.exists(caminho_pdf_contingencia):
                valor_total_fatura = buscar_total_fatura_nubank(caminho_pdf_contingencia)
            else:
                valor_total_fatura = df_compras['Valor'].sum() if not df_compras.empty else 0.0
        elif extensao == '.pdf':
            arquivo_csv_par = caminho_completo.replace('.pdf', '.csv').replace('.PDF', '.csv')
            if os.path.exists(arquivo_csv_par):
                print(f"ℹ️ Ignorando PDF do Nubank porque o CSV equivalente já está na fila.")
                continue
            df_compras = processar_nubank_pdf(caminho_completo, ano_fatura, mes_fatura)
            valor_total_fatura = buscar_total_fatura_nubank(caminho_completo)
            
    else:
        continue

    if df_compras.empty and valor_total_fatura == 0.0:
        continue

    ultimo_acumulado_compras = 0.0

    if not df_compras.empty:
        df_compras['Responsável'] = val_responsavel
        df_compras['Banco'] = val_banco
        df_compras['Período'] = val_periodo
        
        # Cálculo da Soma Acumulada
        df_compras['Fatura Controle'] = df_compras['Valor'].cumsum().round(2)
        if not df_compras['Fatura Controle'].empty:
            ultimo_acumulado_compras = df_compras['Fatura Controle'].iloc[-1]

    soma_compras = df_compras['Valor'].sum() if not df_compras.empty else 0.0
    valor_encargos_calculado = round(valor_total_fatura - soma_compras, 2)

    blocos = [df_compras]

    msg_aviso_padrao = ""
    if fora_do_padrao:
        msg_aviso_padrao = " | 🚨 ATENÇÃO: Renomeie o PDF para o padrão 'AAAA-MM - Descrição - Responsável.pdf'"

    txt_fatura_total = formatar_moeda_texto(valor_total_fatura)
    txt_soma_compras = formatar_moeda_texto(soma_compras)

    fatura_controle_encargos = round(ultimo_acumulado_compras + valor_encargos_calculado, 2)

    if valor_encargos_calculado != 0.0:
        df_encargos = pd.DataFrame([{
            'Responsável': val_responsavel, 'Banco': val_banco, 'Período': val_periodo,
            'Data da Compra': data_fechamento_ajustada,
            'Descrição': 'ENCARGOS E JUROS (CALCULADO VIA REGRA)',
            'Parcela Atual': 1, 'Parcela Total': 1, 
            'Valor': valor_encargos_calculado, 'Tipo': 'Encargos e Juros',
            'Fatura Controle': fatura_controle_encargos,
            'Memória de Cálculo': f"Fórmula Aplicada: {txt_fatura_total} (Total Capa) - {txt_soma_compras} (Soma Compras)" + msg_aviso_padrao
        }])
        blocos.append(df_encargos)

    df_totalizador_visual = pd.DataFrame([{
        'Responsável': val_responsavel, 'Banco': val_banco, 'Período': val_periodo,
        'Data da Compra': data_fechamento_ajustada,
        'Descrição': 'VALOR TOTAL DESTA FATURA (BOLETO PÁG 1)',
        'Parcela Atual': 1, 'Parcela Total': 1, 
        'Valor': 0.0,
        'Tipo': 'Totalizador Fatura',
        'Fatura Controle': valor_total_fatura,
        'Memória de Cálculo': resumo_taxas_mes + msg_aviso_padrao
    }])
    blocos.append(df_totalizador_visual)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        df_final = pd.concat(blocos, ignore_index=True)
        
    colunas_obrigatorias = ['Responsável', 'Banco', 'Período', 'Data da Compra', 'Descrição', 'Parcela Atual', 'Parcela Total', 'Valor', 'Tipo', 'Fatura Controle', 'Memória de Cálculo']
    df_final = df_final[colunas_obrigatorias]

    caminho_excel = os.path.join(PASTA_SAIDA, f"{nome_base} - Movimentações.xlsx")
    df_final.to_excel(caminho_excel, index=False)
    print(f"✔️ Sucesso: Planilha salva em '{caminho_excel}'\n")

print("🚀 Sistema Maestro Concluído! Versão 3.8 rastreando a Data Original Primitiva de todas as parcelas.")