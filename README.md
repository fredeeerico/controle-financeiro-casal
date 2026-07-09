<div align="center">

# Financial Management System

### Case Study — Personal Finance Automation with Excel, Power Query and Python

**Controle Financeiro do Casal**

Excel • Power Query • Python • Data Modeling • Dashboard • Data Governance

Sistema financeiro desenvolvido para simular um fluxo real de organização, tratamento e análise de dados financeiros, utilizando dados sintéticos e documentação técnica para fins de demonstração e portfólio.

![Dashboard Preview](docs/imagens/dashboard-preview.png)

</div>

---

## Objetivo do projeto

Este projeto demonstra como um problema real de controle financeiro familiar pode ser transformado em um sistema estruturado de dados.

A solução organiza contas, cartões, gastos compartilhados, faturas sintéticas, regras de rateio, auditorias e indicadores em um fluxo integrado com Excel, Power Query e Python.

O foco não é apenas criar um dashboard, mas apresentar um processo completo de:

- entrada e organização de dados;
- extração e tratamento de faturas;
- consolidação em base estruturada;
- aplicação de regras de negócio;
- construção de dashboard interativo;
- auditoria, validação e documentação técnica.

---

## Teste rápido

### Dashboard

1. Baixe este repositório.
2. Abra o arquivo:

```text
dashboard/controle-financeiro-casal-dashboard.xlsb
```

3. Use os filtros de **Ano** e **Mês**.
4. Valide se os cards, gráficos e saldo mudam conforme os filtros.
5. Para testar a atualização, use **Dados → Atualizar Tudo** no Microsoft Excel Desktop.

> O arquivo pode ser visualizado pelo Office Online, porém a experiência completa com Power Query, atualização de dados e recursos do dashboard deve ser testada no Microsoft Excel Desktop.

### Extrator de faturas

1. Execute o script:

```text
src/extrator_faturas_casal.py
```

2. Use como entrada as faturas sintéticas disponíveis em:

```text
examples/faturas-sinteticas/input/
```

3. Informe uma pasta vazia como saída.
4. O script irá gerar planilhas estruturadas de movimentações a partir das faturas processadas.

---

## Saiba mais

Este projeto simula um fluxo real de dados financeiros: faturas e movimentações são tratadas por um extrator em Python, consolidadas em uma base estruturada e consumidas por uma planilha com Power Query, tabelas dinâmicas, regras de rateio e dashboard interativo.

A versão publicada utiliza dados sintéticos de 2023 a 2025, criados para representar a saída esperada do extrator de faturas, preservando a privacidade dos dados reais.

O objetivo é demonstrar organização de dados, automação, modelagem de regras de negócio, construção de dashboard, governança e documentação técnica aplicada a um problema real.

---

## Principais funcionalidades

- Dashboard interativo com filtros por ano e mês.
- Separação entre **Contas** e **Cartões**.
- Regra de rateio para gastos compartilhados classificados como **Nosso**.
- Total do casal calculado sem duplicar valores compartilhados.
- Auditoria e fechamento mensal.
- Abas automatizadas para estabelecimentos e recorrências pendentes.
- Power Query portátil para consumo da base sintética.
- Extrator Python para transformar faturas PDF/CSV em planilhas estruturadas.
- Exemplos sintéticos de faturas para testar o extrator sem expor dados reais.
- Documentação técnica para explicar arquitetura, regras e decisões do projeto.

---

## Arquitetura resumida

```text
Faturas PDF/CSV sintéticas
        ↓
Extrator Python
        ↓
Planilhas de movimentações extraídas
        ↓
Base sintética consolidada
        ↓
Power Query + Tabelas Dinâmicas
        ↓
Dashboard financeiro
```

---

## Estrutura do repositório

```text
controle-financeiro-casal/
├── dashboard/                     # Arquivo Excel principal
├── data/synthetic/                # Base sintética consumida pelo Dashboard
├── examples/faturas-sinteticas/   # Faturas sintéticas para testar o extrator
├── src/                           # Código Python do extrator
├── docs/                          # Documentação do projeto
└── _docs_privado/                 # Backlog interno ignorado pelo Git
```

> A pasta `_docs_privado/` é mantida apenas localmente e não deve ser publicada no GitHub.

---

## Explore a documentação

Começando agora?

- [01 - Guia de Teste Rápido](docs/01-guia-teste-rapido.md)  
  Veja como testar o dashboard e o extrator em poucos minutos.

Quer entender como o sistema foi construído?

- [02 - Arquitetura do Sistema](docs/02-arquitetura-do-sistema.md)  
  Fluxo completo dos dados, do extrator ao dashboard.

Quer conhecer a lógica da planilha?

- [03 - Estrutura da Planilha](docs/03-estrutura-da-planilha.md)  
  Descrição das abas, responsabilidades e camadas técnicas.

Quer entender as regras de negócio?

- [04 - Regras de Negócio](docs/04-regras-de-negocio.md)  
  Rateio, contas, cartões, consolidado, saldo e indicadores.

Quer conhecer o extrator?

- [05 - Extrator de Faturas](docs/05-extrator-de-faturas.md)  
  Como PDFs e CSVs são transformados em dados estruturados.

Quer ver a evolução do projeto?

- [06 - Relatório de Desenvolvimento](docs/06-relatorio-de-desenvolvimento.md)  
  Decisões técnicas, melhorias, validações, UX e stress test.

---

## Tecnologias utilizadas

- Microsoft Excel
- Power Query
- Tabelas Dinâmicas
- Segmentadores
- Python
- Pandas
- pdfplumber
- Dados sintéticos

---

## Regras de negócio principais

O sistema trabalha com três tipos de responsáveis:

```text
Fred
Laura
Nosso
```

A regra central é:

- gastos próprios de Fred entram em Fred;
- gastos próprios de Laura entram em Laura;
- gastos compartilhados entram como Nosso;
- os valores classificados como Nosso são rateados 50% para Fred e 50% para Laura;
- o Total Casal é calculado por Fred + Laura, evitando duplicar o valor compartilhado.

Assim, os cards **Contas Nosso** e **Cartões Nosso** funcionam como referência do volume compartilhado, mas não devem ser somados novamente ao Total Casal.

---

## Sobre os dados

Este repositório não contém dados financeiros reais.

As movimentações, faturas, bases e exemplos incluídos foram criados exclusivamente para demonstração técnica do funcionamento do sistema.

O objetivo é permitir que qualquer pessoa teste o dashboard e o extrator sem expor informações pessoais, bancárias ou financeiras reais.

---

## Lições demonstradas pelo projeto

Este case demonstra, na prática, competências importantes para áreas de dados:

- organização de bases e arquivos;
- automação de tratamento de dados;
- modelagem de regras de negócio;
- criação de pipelines locais com Python e Excel;
- uso de Power Query para consolidação;
- construção de dashboards interativos;
- documentação técnica;
- validação por stress test;
- preocupação com privacidade e dados sintéticos;
- visão de governança e manutenção futura.

---

<div align="center">

### Desenvolvido como projeto de portfólio

Gestão de Dados • Engenharia de Dados • Análise de Dados

</div>
