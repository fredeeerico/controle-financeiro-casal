# Estrutura da Planilha

## Visão Geral

A planilha foi organizada em camadas com responsabilidades bem definidas.

Essa divisão reduz a complexidade operacional, facilita a manutenção do sistema e separa claramente as áreas de entrada de dados, processamento, auditoria e apresentação.

---

# Organização das Abas

## Dashboard

**Objetivo**

Camada de apresentação do sistema.

É a principal interface utilizada pelo usuário para acompanhar indicadores financeiros e realizar análises.

### Principais recursos

- Cards de indicadores
- Gráficos interativos
- Segmentadores de Ano e Mês
- Consolidação por responsável
- Comparação entre Contas e Cartões
- Evolução do saldo
- Gastos por categoria

---

## Contas

**Objetivo**

Registrar movimentações que não são provenientes de faturas de cartão.

Exemplos:

- Salários
- Contas domésticas
- Boletos
- Recebimentos
- Transferências

Essa aba também contém fórmulas responsáveis por automatizar parte do preenchimento dos registros.

---

## Estabelecimentos

**Objetivo**

Padronizar nomes de estabelecimentos e automatizar sua classificação.

Permite que diferentes descrições para um mesmo local sejam consolidadas em um único nome padronizado, reduzindo inconsistências nas análises.

---

## Auditoria e Fechamento

**Objetivo**

Centralizar verificações realizadas durante o fechamento financeiro mensal.

Essa aba auxilia na conferência das movimentações importadas, identificação de inconsistências e validação do processo antes da atualização do Dashboard.

---

## Estab Pendentes

**Objetivo**

Listar automaticamente estabelecimentos ainda não classificados.

Funciona como apoio ao processo de padronização da base.

O usuário apenas consulta essa aba quando necessário.

---

## Recorrências Pendentes

**Objetivo**

Identificar automaticamente movimentações que podem representar despesas recorrentes ainda não cadastradas.

Serve como ferramenta de apoio para evolução contínua da base.

---

## Dashboard_Base

**Objetivo**

Camada técnica responsável por alimentar o Dashboard.

Concentra tabelas auxiliares, cálculos e estruturas utilizadas pelos gráficos e indicadores.

Essa aba permanece oculta durante o uso normal do sistema.

---

## Configurações

**Objetivo**

Centralizar parâmetros e tabelas auxiliares utilizadas pelo sistema.

Essa estrutura facilita futuras evoluções sem necessidade de alterar fórmulas espalhadas pela planilha.

---

## Abas Ocultas

As abas abaixo possuem função exclusivamente técnica.

Não devem ser editadas diretamente.

- Movimentações
- Movimentações Cartões
- Categorias

Essas abas são utilizadas pelo Power Query e pelas Tabelas Dinâmicas que alimentam o Dashboard.

---

# Organização por Camadas

```text
Usuário

↓

Dashboard

↓

Dashboard_Base

↓

Power Query

↓

Movimentações

↓

Extrator Python

↓

Faturas PDF / CSV
```

---

# Convenção de Cores

Para facilitar a utilização do sistema, as abas foram organizadas por cores.

## 🟢 Verde

Abas destinadas ao uso cotidiano.

Podem receber edição e interação do usuário.

Exemplos:

- Dashboard
- Contas
- Estabelecimentos
- Auditoria e Fechamento

---

## 🟣 Roxo

Abas automatizadas.

Funcionam como apoio operacional e normalmente apenas são consultadas.

Exemplos:

- Estab Pendentes
- Recorrências Pendentes

---

## 🟡 Amarelo

Abas técnicas utilizadas como fonte de dados.

Alterações devem ser realizadas apenas quando houver necessidade de manutenção do sistema.

Exemplos:

- Dashboard_Base
- Configurações

---

# Filosofia de Desenvolvimento

Durante a construção do projeto foi adotado um princípio simples:

> Tornar a experiência do usuário o mais simples possível, mantendo a complexidade concentrada nas camadas técnicas.

Essa abordagem reduz erros operacionais e facilita futuras evoluções do sistema.

---

## Próximo documento

➡️ **04 - Regras de Negócio**

Neste documento são apresentadas todas as regras utilizadas para cálculos, consolidações e indicadores do sistema.