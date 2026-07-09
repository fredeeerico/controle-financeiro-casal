# Relatório de Desenvolvimento

## Resumo

O **Controle Financeiro do Casal** foi desenvolvido como um estudo de caso para demonstrar a aplicação de conceitos de Gestão de Dados, Engenharia de Dados e Análise de Dados na resolução de um problema real.

Embora tenha sido concebido para organizar as finanças de um casal, o projeto evoluiu para um sistema estruturado de tratamento de dados, composto por automação, modelagem, documentação técnica e visualização analítica.

---

# O problema

O controle financeiro era realizado de forma predominantemente manual, exigindo:

- importação manual de faturas;
- classificação repetitiva de estabelecimentos;
- consolidação de diferentes instituições financeiras;
- atualização manual de análises.

Esse processo consumia tempo, aumentava a probabilidade de erros e dificultava auditorias e análises históricas.

---

# Objetivos do Projeto

Os principais objetivos definidos durante o desenvolvimento foram:

- reduzir tarefas manuais;
- padronizar a organização dos dados;
- automatizar a importação de movimentações;
- consolidar informações de diferentes fontes;
- disponibilizar indicadores claros para tomada de decisão;
- construir uma solução fácil de manter e evoluir.

---

# Evolução da Solução

O projeto evoluiu em etapas.

## Fase 1 — Organização

Estruturação da pasta do projeto, definição da arquitetura de arquivos e criação da planilha principal.

---

## Fase 2 — Modelagem

Definição das tabelas, categorias, responsáveis, cartões e regras de negócio.

---

## Fase 3 — Automação

Desenvolvimento do extrator de faturas em Python para processar documentos Santander (PDF) e Nubank (CSV).

---

## Fase 4 — Consolidação

Integração da base através do Power Query e construção das tabelas dinâmicas.

---

## Fase 5 — Dashboard

Desenvolvimento do painel interativo com indicadores, gráficos e filtros por Ano e Mês.

---

## Fase 6 — Auditoria e Experiência do Usuário

Reorganização das abas, definição de cores por responsabilidade, proteção de áreas críticas, simplificação da navegação e criação da área de Auditoria e Fechamento.

---

## Fase 7 — Documentação e Portfólio

Substituição dos dados reais por dados sintéticos, criação das faturas de exemplo, documentação técnica e preparação do repositório para publicação no GitHub.

---

# Principais Decisões Técnicas

Durante o desenvolvimento foram adotadas algumas decisões importantes.

## Separação em camadas

O sistema foi dividido entre:

- entrada dos dados;
- processamento;
- consolidação;
- apresentação.

Essa separação reduz o acoplamento e facilita futuras evoluções.

---

## Dados sintéticos

Todos os dados publicados foram substituídos por informações sintéticas.

Essa decisão permite compartilhar o projeto sem expor informações pessoais ou financeiras.

---

## Power Query portátil

A estrutura foi ajustada para permitir a atualização da base em diferentes computadores sem necessidade de reconfiguração completa.

---

## Padronização

Foram criadas tabelas auxiliares para padronizar:

- estabelecimentos;
- categorias;
- responsáveis;
- cartões.

Isso melhora a qualidade das análises e reduz inconsistências.

---

# Validações Realizadas

Antes da publicação foram realizados testes para validar:

- atualização automática do Power Query;
- funcionamento do Dashboard;
- filtros por Ano e Mês;
- consolidação entre Contas e Cartões;
- regra de rateio para gastos compartilhados;
- cálculo do Total do Casal;
- funcionamento do extrator de faturas;
- proteção das áreas críticas da planilha.

Todos os testes foram concluídos com sucesso utilizando a base sintética publicada.

---

# Competências Demonstradas

Este projeto permitiu aplicar conhecimentos relacionados a:

- Excel Avançado;
- Power Query;
- Modelagem de Dados;
- Limpeza e Padronização de Dados;
- Automação com Python;
- Documentação Técnica;
- Governança de Dados;
- Construção de Dashboards;
- Organização de Projetos;
- Controle de Versão com Git e GitHub.

---

# Limitações Conhecidas

A versão atual foi desenvolvida como prova de conceito.

Entre as principais limitações estão:

- suporte apenas para Santander (PDF) e Nubank (CSV);
- utilização de base sintética para demonstração;
- execução local do extrator.

Essas limitações foram mantidas intencionalmente para preservar simplicidade, reprodutibilidade e foco didático.

---

# Próximos Passos

A arquitetura foi planejada para permitir futuras evoluções, como:

- suporte a novas instituições financeiras;
- parametrização dos responsáveis (substituindo "Fred", "Laura" e "Nosso" por nomes configuráveis);
- ampliação das automações;
- novos indicadores analíticos;
- melhorias contínuas na experiência do usuário.

---

# Conclusão

Mais do que um dashboard financeiro, este projeto representa um estudo de caso sobre organização, tratamento e análise de dados aplicados a um problema cotidiano.

O desenvolvimento priorizou boas práticas de documentação, separação de responsabilidades, automação e qualidade dos dados, buscando construir uma solução de fácil manutenção e evolução.