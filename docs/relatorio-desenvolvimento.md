# Relatório de Desenvolvimento e Governança

## Visão geral

O projeto Controle Financeiro do Casal nasceu de uma necessidade real de organizar contas, cartões, gastos compartilhados e fechamento mensal.

A solução evoluiu de uma planilha de controle financeiro para um sistema em Excel com Power Query, tabelas dinâmicas, regras de negócio, extrator Python, dashboard interativo, documentação e validações de portfólio.

## Objetivo

Construir um sistema simples para uso operacional, mas robusto o suficiente para demonstrar competências em dados:

- Organização de dados.
- Modelagem de regras de negócio.
- Automação com Python.
- Power Query.
- Dashboard.
- Governança e documentação.
- Testes e validação.

## Evolução do sistema

### 1. Estrutura inicial

Foram definidas abas para contas, estabelecimentos, movimentações, categorias, configurações e dashboard.

### 2. Base sintética

Para publicação no GitHub, os dados reais foram substituídos por uma base sintética de 2023 a 2025. Essa base preserva a estrutura analítica do sistema sem expor dados reais.

### 3. Power Query portátil

A conexão com a base foi ajustada para não depender de caminhos locais. Foi criada a tabela `tb_parametros_repositorio`, permitindo que a planilha localize a base sintética dentro da estrutura do repositório.

### 4. Dashboard

O Dashboard foi construído com cards, gráficos e segmentadores para análise por ano e mês.

Indicadores principais:

- Contas Fred.
- Contas Laura.
- Contas Nosso.
- Cartões Fred.
- Cartões Laura.
- Cartões Nosso.
- Total Fred.
- Total Laura.
- Total Nosso.
- Total Casal.
- Saldo.

### 5. Regra de rateio

Foi validado que Fred e Laura recebem 50% dos valores classificados como Nosso. Os cards Nosso aparecem como referência do volume compartilhado e não devem ser somados novamente ao Total Casal.

### 6. UX e organização de abas

As abas Início e Início - Base foram removidas após validação funcional. A aba Dashboard passou a ser o painel principal.

A aba Auditoria e Fechamento foi reorganizada como painel executivo de controle mensal.

A Dashboard_Base foi reorganizada como camada técnica de apoio, com títulos e descrições para facilitar investigação por recrutadores.

### 7. Proteções aplicadas

Foram aplicadas proteções seletivas:

- Dashboard protegido contra edição acidental, mantendo filtros clicáveis.
- Contas com cabeçalhos e fórmulas protegidos.
- Estabelecimentos com cabeçalhos protegidos.
- Abas automatizadas mantidas sem proteção para não impedir atualizações de dados externos.

### 8. Correções críticas

- Remoção de dependência de caminho local `G:\`.
- Correção do gráfico Evolução do Saldo Mensal para reconhecer 2025.
- Ajuste das conexões dos filtros de Ano e Mês.
- Renomeação dos cards para diferenciar Contas e Cartões.

### 9. Stress test

O Dashboard foi validado com diferentes filtros:

- Ano completo.
- Mês específico.
- Visão geral completa.
- Casos de saldo positivo e negativo.

Foram validados:

- Cards.
- Gráficos.
- Rateio do Nosso.
- Saldo.
- Total Casal sem duplicidade.
- Atualização geral.

## Estado final

A versão publicada está preparada para demonstração em portfólio, com dados sintéticos, documentação, faturas sintéticas para teste do extrator e Dashboard funcional.
