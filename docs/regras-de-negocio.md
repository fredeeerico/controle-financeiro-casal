# Regras de Negócio

## Responsáveis

O sistema trabalha com três classificações principais:

- **Fred**: gastos individuais do Fred.
- **Laura**: gastos individuais da Laura.
- **Nosso**: gastos compartilhados do casal.

## Regra de rateio do Nosso

Os gastos classificados como **Nosso** são compartilhados em 50% para Fred e 50% para Laura.

Isso significa que:

```text
Total Fred = Gastos próprios do Fred + 50% dos gastos Nosso
Total Laura = Gastos próprios da Laura + 50% dos gastos Nosso
Total Casal = Total Fred + Total Laura
```

O valor **Nosso** é exibido como referência do volume compartilhado, mas não deve ser somado novamente ao Total Casal.

## Contas e Cartões

O Dashboard separa duas origens de gastos:

- **Contas**: lançamentos manuais ou despesas registradas diretamente na planilha.
- **Cartões**: movimentações vindas de faturas/importações.

Os cards individuais de Contas e Cartões já consideram o rateio de 50% do Nosso.

## Saldo

O saldo é calculado a partir das receitas menos o total de despesas do casal no período filtrado.

```text
Saldo = Receitas - Total Casal
```

## Decisão importante de visualização

O gráfico `Evolução Mensal por Responsável` preserva a visão histórica do ano e não é filtrado por mês. Essa decisão foi tomada para manter a leitura da evolução temporal.

O gráfico `Evolução do Saldo Mensal`, por outro lado, respeita os filtros de Ano e Mês.
