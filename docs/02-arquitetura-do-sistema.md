# Arquitetura do Sistema

## Visão Geral

O Controle Financeiro do Casal foi projetado como um sistema de processamento de dados financeiros, dividido em camadas independentes.

Essa arquitetura permite que cada etapa tenha uma responsabilidade específica, facilitando manutenção, evolução e reutilização dos componentes.

---

# Fluxo Geral

```text
Faturas PDF / CSV
        │
        ▼
Extrator Python
        │
        ▼
Planilhas de Movimentações
        │
        ▼
Base Sintética Consolidada
        │
        ▼
Power Query
        │
        ▼
Tabelas Dinâmicas
        │
        ▼
Dashboard Financeiro
```

Cada camada possui uma função específica.

---

# 1. Entrada dos Dados

O sistema recebe documentos financeiros em dois formatos:

- PDF (Santander)
- CSV (Nubank)

Todos os arquivos seguem um padrão de nomenclatura para permitir sua identificação automática.

Exemplo:

```text
AAAA-MM - Fatura Santander - Fred.pdf

AAAA-MM - Fatura Nubank - Laura.csv
```

A nomenclatura permite identificar:

- período;
- instituição financeira;
- responsável.

---

# 2. Extrator de Faturas

O extrator, desenvolvido em Python, é responsável por:

- identificar automaticamente o banco;
- identificar o responsável;
- identificar o período;
- extrair cada movimentação;
- calcular encargos quando necessário;
- gerar planilhas estruturadas.

Cada documento processado gera uma planilha de movimentações independente.

---

# 3. Base Consolidada

As planilhas produzidas pelo extrator representam a camada intermediária do sistema.

Essas planilhas são posteriormente consolidadas em uma base sintética utilizada pelo Dashboard.

Essa abordagem permite demonstrar todo o funcionamento do projeto sem expor dados financeiros reais.

---

# 4. Power Query

O Power Query é responsável por:

- importar automaticamente a base consolidada;
- transformar os dados;
- aplicar padronizações;
- atualizar as tabelas utilizadas pelo Dashboard.

Toda a lógica de atualização permanece centralizada nesta camada.

---

# 5. Modelo Analítico

Após o tratamento dos dados, o sistema alimenta diversas tabelas dinâmicas responsáveis por gerar:

- indicadores;
- gráficos;
- cartões;
- análises temporais;
- comparações entre contas e cartões.

Essa camada funciona como o modelo analítico do projeto.

---

# 6. Dashboard

O Dashboard representa a camada de apresentação.

Seu objetivo é transformar dados estruturados em informações facilmente interpretáveis.

Entre os principais recursos disponíveis estão:

- filtros por Ano;
- filtros por Mês;
- indicadores financeiros;
- evolução do saldo;
- distribuição por categoria;
- comparação entre contas e cartões;
- consolidação por responsável.

---

# Arquitetura em Camadas

```text
Camada 1
Entrada dos Arquivos

↓

Camada 2
Extração (Python)

↓

Camada 3
Base Estruturada

↓

Camada 4
Power Query

↓

Camada 5
Modelo Analítico

↓

Camada 6
Dashboard
```

---

# Benefícios desta arquitetura

- Separação de responsabilidades.
- Facilidade de manutenção.
- Reutilização das bases.
- Automatização do tratamento de dados.
- Escalabilidade para novas instituições financeiras.
- Facilidade para auditoria e validação dos dados.

---

## Próximo documento

➡️ **03 - Estrutura da Planilha**

Neste documento são apresentadas todas as abas do sistema, suas responsabilidades e a forma como se relacionam.