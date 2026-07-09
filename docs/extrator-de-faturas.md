# Extrator de Faturas

O arquivo `src/extrator_faturas_casal.py` é um script Python criado para transformar faturas em planilhas estruturadas de movimentações.

## O que ele faz

- Lê uma pasta de entrada com arquivos PDF e CSV.
- Identifica banco, responsável e período a partir do nome do arquivo.
- Processa PDFs Santander.
- Processa CSVs Nubank.
- Gera uma planilha Excel por fatura processada.
- Inclui informações de controle, como valor acumulado da fatura e memória de cálculo.

## Padrão de nome esperado

```text
AAAA-MM - Fatura Banco - Responsável.extensão
```

Exemplos:

```text
2026-01 - Fatura Santander - Fred.pdf
2026-01 - Fatura Nubank - Fred.csv
2026-03 - Fatura Santander - Nosso.pdf
```

## Campos gerados

As planilhas de saída geradas pelo extrator seguem a estrutura:

```text
Responsável
Banco
Período
Data da Compra
Descrição
Parcela Atual
Parcela Total
Valor
Tipo
Fatura Controle
Memória de Cálculo
```

## Como testar

Use os arquivos sintéticos em:

```text
examples/faturas-sinteticas/input/
```

Execute o script:

```bash
python src/extrator_faturas_casal.py
```

Quando solicitado, informe:

```text
Pasta de entrada: examples/faturas-sinteticas/input
Pasta de saída: examples/faturas-sinteticas/output
```

## Observação sobre a base sintética

A base `data/synthetic/portfolio-movimentacoes-2023-2025.xlsx` simula o resultado consolidado esperado após processos de extração e organização das faturas.

Ela foi criada para demonstrar o Dashboard sem expor dados financeiros reais.
