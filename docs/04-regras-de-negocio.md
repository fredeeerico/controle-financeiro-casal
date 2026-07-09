# Regras de Negócio

## Visão Geral

O Dashboard não realiza cálculos diretamente.

Todas as informações apresentadas são resultado de regras de negócio aplicadas sobre uma base estruturada de movimentações financeiras.

Este documento descreve as principais regras utilizadas pelo sistema.

---

# Responsáveis

O sistema trabalha com três tipos de responsáveis:

- Fred
- Laura
- Nosso

Cada movimentação pertence obrigatoriamente a um desses responsáveis.

---

# Contas x Cartões

O sistema separa movimentações em dois grupos.

## Contas

Representam movimentações financeiras que não pertencem a cartões de crédito.

Exemplos:

- Salário
- Recebimentos
- Água
- Energia
- Internet
- Boletos
- Transferências

---

## Cartões

Representam despesas provenientes das faturas dos cartões de crédito.

Essas movimentações são importadas automaticamente através do Extrator de Faturas.

---

# Gastos Compartilhados

Quando uma movimentação pertence ao casal, ela recebe o responsável:

```text
Nosso
```

Essas movimentações permanecem registradas integralmente na base.

O rateio ocorre apenas durante a geração dos indicadores.

---

# Regra de Rateio

Toda movimentação classificada como **Nosso** é dividida igualmente entre Fred e Laura.

```text
Nosso
      ↓

50% Fred

50% Laura
```

Essa regra garante que cada pessoa visualize corretamente sua participação nas despesas compartilhadas.

---

# Total Fred

É composto por:

- Gastos próprios de Fred;
- 50% dos gastos classificados como Nosso.

---

# Total Laura

É composto por:

- Gastos próprios de Laura;
- 50% dos gastos classificados como Nosso.

---

# Total Casal

O indicador Total Casal é calculado pela soma dos totais de Fred e Laura.

Como o rateio já ocorreu anteriormente, o valor compartilhado não é contabilizado duas vezes.

---

# Cards "Nosso"

Os cards:

- Contas Nosso
- Cartões Nosso

não representam valores adicionais.

Seu objetivo é apenas informar quanto do total corresponde às despesas compartilhadas.

Esses valores não devem ser somados novamente ao Total Casal.

---

# Separação entre Contas e Cartões

Todos os indicadores do Dashboard respeitam a separação entre:

- Contas
- Cartões

Isso permite análises independentes para cada origem das movimentações.

---

# Atualização Automática

Após novas movimentações serem adicionadas à base, o processo ocorre na seguinte ordem:

```text
Nova Base

↓

Power Query

↓

Movimentações

↓

Tabelas Dinâmicas

↓

Dashboard
```

Nenhuma alteração manual é necessária nos gráficos.

---

# Auditoria

Antes da atualização do Dashboard, recomenda-se validar:

- movimentações pendentes;
- estabelecimentos não classificados;
- recorrências pendentes;
- consistência das importações.

Essas verificações reduzem inconsistências nas análises.

---

# Dados Sintéticos

Toda a versão publicada utiliza dados sintéticos.

Isso permite:

- preservar a privacidade;
- disponibilizar exemplos completos;
- validar o funcionamento do sistema;
- demonstrar o pipeline de dados sem utilizar informações reais.

---

# Princípios adotados

Durante o desenvolvimento do projeto foram seguidos os seguintes princípios:

- simplicidade para o usuário;
- automação sempre que possível;
- separação entre entrada, processamento e apresentação;
- documentação das decisões;
- facilidade de manutenção;
- possibilidade de evolução futura.

---

## Próximo documento

➡️ **05 - Extrator de Faturas**

Neste documento é apresentado o funcionamento do componente responsável por transformar faturas PDF e CSV em dados estruturados utilizados pelo sistema.