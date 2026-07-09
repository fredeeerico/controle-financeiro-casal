# Relatório de Desenvolvimento

## Resumo

O **Controle Financeiro do Casal** foi desenvolvido como um estudo de caso para demonstrar a aplicação de conceitos de Gestão de Dados, Engenharia de Dados e Análise de Dados na resolução de um problema real.

Embora tenha surgido da necessidade de organizar as finanças de um casal, o projeto evoluiu para um sistema estruturado de tratamento de dados, combinando automação, modelagem de informações, documentação técnica e visualização analítica.

---

# Contexto

O processo de controle financeiro era realizado de forma predominantemente manual, envolvendo lançamentos recorrentes, importação de faturas, classificação de despesas e consolidação de informações provenientes de diferentes instituições financeiras.

Com o aumento da quantidade de dados, tornou-se necessário estruturar uma solução que reduzisse tarefas repetitivas, aumentasse a confiabilidade das informações e facilitasse análises mensais.

---

# Objetivos

Durante o desenvolvimento foram definidos os seguintes objetivos:

- reduzir atividades manuais;
- padronizar a organização dos dados;
- automatizar a importação de movimentações financeiras;
- consolidar dados provenientes de diferentes fontes;
- disponibilizar indicadores claros para tomada de decisão;
- construir uma solução simples para utilização diária e fácil de manter.

---

# Evolução do Projeto

O desenvolvimento foi realizado de forma incremental.

## Fase 1 — Estruturação

- Organização das pastas do projeto.
- Definição da arquitetura inicial.
- Construção da planilha principal.

---

## Fase 2 — Modelagem

- Estruturação das tabelas.
- Definição das categorias.
- Cadastro de cartões.
- Definição dos responsáveis.
- Criação das primeiras regras de negócio.

---

## Fase 3 — Automação

Desenvolvimento do extrator de faturas em Python para processamento de:

- Santander (PDF)
- Nubank (CSV)

O objetivo foi transformar documentos financeiros em planilhas estruturadas.

---

## Fase 4 — Integração dos Dados

Implementação do Power Query para:

- importar automaticamente as bases;
- transformar os dados;
- consolidar as movimentações;
- alimentar o Dashboard.

---

## Fase 5 — Dashboard

Construção do painel principal contendo:

- indicadores financeiros;
- gráficos;
- segmentadores;
- comparações entre contas e cartões;
- análises temporais.

---

## Fase 6 — Experiência do Usuário

Foram realizados diversos ajustes visando facilitar o uso diário do sistema.

Entre eles:

- reorganização das abas;
- padronização visual;
- definição de cores por responsabilidade;
- proteção de áreas críticas;
- criação da área de Auditoria e Fechamento;
- ocultação das abas técnicas.

---

## Fase 7 — Publicação

Antes da disponibilização do projeto foram realizados:

- substituição dos dados reais por dados sintéticos;
- criação de faturas sintéticas para testes;
- documentação técnica;
- organização do repositório no GitHub.

---

# Decisões Técnicas

Algumas decisões foram fundamentais durante o desenvolvimento.

## Separação em camadas

O sistema foi dividido em:

- entrada dos dados;
- processamento;
- consolidação;
- apresentação.

Essa abordagem facilita manutenção, evolução e reutilização dos componentes.

---

## Utilização de Dados Sintéticos

Todos os dados disponibilizados publicamente foram substituídos por informações sintéticas.

Essa decisão preserva a privacidade das informações financeiras sem comprometer a capacidade de demonstrar o funcionamento do sistema.

---

## Organização da Planilha

As abas foram organizadas conforme sua finalidade:

- operação;
- apoio;
- processamento;
- apresentação.

Também foi definida uma convenção de cores para facilitar a identificação das áreas editáveis e técnicas.

---

## Padronização

Foram criadas estruturas auxiliares para padronizar:

- estabelecimentos;
- categorias;
- cartões;
- responsáveis.

Essa padronização reduz inconsistências e melhora a qualidade das análises.

---

# Validação da Solução

Antes da publicação foram realizados testes para validar:

- atualização do Power Query;
- funcionamento dos filtros;
- atualização automática dos indicadores;
- consolidação entre Contas e Cartões;
- regra de rateio dos gastos compartilhados;
- funcionamento do Dashboard;
- funcionamento do extrator de faturas;
- proteção das áreas críticas da planilha.

Todos os testes foram executados utilizando a base sintética publicada neste repositório.

---

# Competências Demonstradas

Durante o desenvolvimento foram aplicados conhecimentos relacionados a:

- Excel Avançado;
- Power Query;
- Python;
- Pandas;
- Modelagem de Dados;
- Limpeza e Padronização de Dados;
- Documentação Técnica;
- Organização de Projetos;
- Git e GitHub;
- Construção de Dashboards.

---

# Limitações da Versão Atual

A versão publicada possui algumas limitações conhecidas:

- suporte às faturas Santander (PDF) e Nubank (CSV);
- execução local do extrator;
- utilização de dados sintéticos.

Essas decisões foram adotadas para manter o projeto simples, reproduzível e adequado à finalidade de demonstração técnica.

---

# Evoluções Futuras

A arquitetura foi planejada para permitir futuras evoluções, entre elas:

- inclusão de novas instituições financeiras;
- parametrização dos responsáveis (substituindo "Fred", "Laura" e "Nosso" por nomes configuráveis);
- ampliação das automações;
- novos indicadores analíticos;
- melhorias contínuas na experiência do usuário.

---

# Conclusão

Este projeto demonstra como um problema cotidiano pode ser transformado em uma solução estruturada utilizando conceitos de organização, tratamento e análise de dados.

Além do Dashboard, o foco foi desenvolver um fluxo completo de processamento, documentar as decisões tomadas e construir uma solução de fácil manutenção, capaz de evoluir conforme novas necessidades surgirem.
