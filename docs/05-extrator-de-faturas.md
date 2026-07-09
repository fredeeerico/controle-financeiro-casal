# Extrator de Faturas

## Visão Geral

O Extrator de Faturas é o componente responsável por transformar documentos financeiros em uma base estruturada de movimentações, utilizada posteriormente pelo Dashboard.

Nesta versão do projeto, o extrator suporta:

- Faturas Santander (PDF)
- Faturas Nubank (CSV)

Sua principal função é reduzir o trabalho manual de importação, padronizando os dados antes que sejam consumidos pelo Power Query.

---

# Fluxo de Funcionamento

```text
Faturas PDF / CSV
        │
        ▼
Identificação do Banco
        │
        ▼
Identificação do Responsável
        │
        ▼
Extração das Movimentações
        │
        ▼
Tratamento e Padronização
        │
        ▼
Planilha Excel Estruturada
```

Cada fatura gera uma planilha independente contendo todas as movimentações identificadas.

---

# Estrutura Esperada

As faturas devem estar organizadas em uma pasta de entrada.

Exemplo:

```text
examples/
└── faturas-sinteticas/
    └── input/
        ├── 2026-01 - Fatura Santander - Fred.pdf
        ├── 2026-01 - Fatura Nubank - Fred.csv
        ├── 2026-02 - Fatura Santander - Laura.pdf
        ├── 2026-02 - Fatura Nubank - Laura.csv
        ├── 2026-03 - Fatura Santander - Nosso.pdf
        └── 2026-03 - Fatura Nubank - Nosso.csv
```

O nome do arquivo é utilizado para identificar automaticamente:

- Banco
- Responsável
- Período

---

# Como executar

## 1. Instale as dependências

Abra um terminal na raiz do projeto e execute:

```bash
pip install -r requirements.txt
```

---

## 2. Execute o programa

```bash
python src/extrator_faturas_casal.py
```

---

## 3. Informe a pasta de entrada

Quando solicitado, selecione a pasta:

```text
examples/faturas-sinteticas/input/
```

---

## 4. Informe a pasta de saída

Escolha uma pasta vazia.

Exemplo:

```text
examples/faturas-sinteticas/output/
```

---

## 5. Aguarde o processamento

O programa irá:

- localizar todas as faturas;
- identificar automaticamente o banco;
- processar cada documento;
- gerar uma planilha Excel para cada fatura.

---

# Resultado Esperado

Ao final da execução, a pasta de saída deverá conter planilhas estruturadas correspondentes às faturas processadas.

Exemplo:

```text
output/

2026-01 - Santander - Fred.xlsx
2026-01 - Nubank - Fred.xlsx

2026-02 - Santander - Laura.xlsx
2026-02 - Nubank - Laura.xlsx

2026-03 - Santander - Nosso.xlsx
2026-03 - Nubank - Nosso.xlsx
```

Essas planilhas representam a camada intermediária utilizada posteriormente pelo Dashboard.

---

# Tratamentos Realizados

Durante o processamento, o extrator realiza automaticamente:

- identificação do banco;
- identificação do responsável;
- identificação do período;
- leitura das movimentações;
- limpeza dos dados;
- padronização da estrutura;
- geração da planilha final.

---

# Integração com o Dashboard

Após a geração das planilhas:

```text
Planilhas Extraídas

↓

Base Consolidada

↓

Power Query

↓

Dashboard
```

Basta atualizar o Dashboard utilizando:

```text
Dados → Atualizar Tudo
```

---

# Limitações da Versão Atual

Esta versão foi desenvolvida para fins de demonstração técnica.

Atualmente suporta:

- Santander PDF
- Nubank CSV

A arquitetura foi planejada para permitir a inclusão de novas instituições financeiras futuramente, sem necessidade de alterar o restante do sistema.

---

# Próximo documento

➡️ **06 - Relatório de Desenvolvimento**

Este documento apresenta a evolução completa do projeto, decisões técnicas, melhorias implementadas, testes realizados e aprendizados obtidos durante o desenvolvimento.