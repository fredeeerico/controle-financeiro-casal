# Guia de Teste Rápido

Este guia mostra como validar rapidamente se o projeto está funcionando.

## 1. Testar o Dashboard

Abra:

```text
dashboard/controle-financeiro-casal-dashboard.xlsb
```

No Excel, use os segmentadores do Dashboard.

### Teste A — visão geral completa

Filtro:

```text
Ano = todos
Mês = todos
```

Valide:

- Cards mostram o consolidado geral da base 2023–2025.
- Gráfico `Gastos por Categoria` mostra a composição completa.
- Gráfico `Contas x Cartão` mostra múltiplos períodos.
- Gráfico `Evolução do Saldo Mensal` mostra a série completa.

### Teste B — ano completo

Filtro:

```text
Ano = 2025
Mês = todos
```

Valide:

- Cards mudam para o ano de 2025.
- Gráfico `Evolução do Saldo Mensal` mostra os meses de 2025.
- `Total Casal = Total Fred + Total Laura`.
- `Total Nosso` aparece como referência de gastos compartilhados, sem ser somado novamente ao Total Casal.

### Teste C — mês específico

Filtro:

```text
Ano = 2025
Mês = abr
```

Valide:

- Cards mostram apenas abril de 2025.
- Gráfico `Contas x Cartão` mostra somente abril.
- Gráfico `Evolução do Saldo Mensal` mostra somente `abr/25`.
- Gráfico `Evolução Mensal por Responsável` mantém o histórico anual, conforme decisão de design.

## 2. Testar atualização

No Excel:

```text
Dados → Atualizar Tudo
```

Resultado esperado:

- Sem erro de Power Query.
- Sem referência a caminhos locais antigos.
- Dashboard continua respondendo aos filtros.

## 3. Testar o extrator

Siga o guia em:

```text
examples/faturas-sinteticas/README.md
```
