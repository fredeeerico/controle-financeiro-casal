# Arquitetura do Sistema

O projeto foi estruturado como um fluxo de dados simples e auditável.

```text
Faturas PDF/CSV
      ↓
Extrator Python
      ↓
Planilhas de movimentações extraídas
      ↓
Base consolidada sintética
      ↓
Power Query
      ↓
Tabelas dinâmicas e bases auxiliares
      ↓
Dashboard
```

## Camadas

### 1. Entrada de dados

A entrada pode vir de:

- Faturas Santander em PDF.
- Faturas Nubank em CSV.
- Lançamentos manuais na aba `Contas`.

No repositório público, os arquivos de fatura são sintéticos.

### 2. Extração

O script `src/extrator_faturas_casal.py` lê uma pasta de entrada com PDFs/CSVs e gera planilhas Excel de movimentações.

Ele identifica informações pelo nome do arquivo, como:

- Ano e mês da fatura.
- Banco.
- Responsável: Fred, Laura ou Nosso.

### 3. Base sintética

A base em `data/synthetic/portfolio-movimentacoes-2023-2025.xlsx` representa um conjunto consolidado de movimentações para demonstração do Dashboard.

Ela simula a estrutura esperada após o processamento das faturas pelo extrator, sem expor dados reais.

### 4. Excel e Power Query

A planilha principal consome a base sintética usando Power Query. A configuração foi ajustada para ser portátil e não depender de caminhos locais do computador do autor.

### 5. Dashboard

O Dashboard usa tabelas dinâmicas, segmentadores e bases auxiliares para apresentar:

- Contas.
- Cartões.
- Gastos compartilhados.
- Gastos por categoria.
- Contas x Cartões.
- Evolução mensal por responsável.
- Evolução do saldo mensal.
