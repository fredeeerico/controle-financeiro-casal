# Guia de Teste Rápido

## Objetivo

Este guia foi criado para que qualquer pessoa consiga validar o funcionamento do projeto em poucos minutos, sem necessidade de conhecer sua implementação.

---

# Testando o Dashboard

## Requisitos

- Microsoft Excel (Desktop)
- Conteúdo habilitado
- Power Query habilitado

---

## Passo 1

Abra o arquivo:

```text
dashboard/controle-financeiro-casal-dashboard.xlsb
```

---

## Passo 2

Acesse a aba **Dashboard**.

---

## Passo 3

Utilize os filtros disponíveis.

Experimente, por exemplo:

```text
Ano = 2025
Mês = Abril
```

Valide que:

- Todos os cards são atualizados.
- Os gráficos respondem aos filtros.
- O saldo mensal muda corretamente.
- Os gastos são separados entre Contas e Cartões.

---

## Passo 4

Teste outros períodos:

```text
2024
Julho
```

```text
2025
Setembro
```

```text
Todos os anos
Todos os meses
```

Verifique que o Dashboard permanece consistente em todas as combinações.

---

# Testando o Extrator

Execute o arquivo:

```text
src/extrator_faturas_casal.py
```

Informe como entrada:

```text
examples/faturas-sinteticas/input/
```

Escolha uma pasta vazia para saída.

---

## Resultado esperado

O sistema deverá:

- identificar automaticamente o banco;
- identificar o responsável;
- identificar o período da fatura;
- extrair as movimentações;
- gerar uma planilha Excel para cada documento processado.

---

# Atualizando o Dashboard

Após gerar novas planilhas:

1. Abra o Dashboard.
2. Clique em:

```text
Dados → Atualizar Tudo
```

O Dashboard deverá refletir automaticamente a base consolidada.

---

# Validações realizadas

Durante o desenvolvimento deste projeto foram realizados testes para validar:

- atualização automática do Power Query;
- funcionamento dos filtros;
- regras de rateio;
- consolidação de contas e cartões;
- cálculo do Total do Casal;
- cálculo do Saldo;
- funcionamento do extrator;
- compatibilidade com dados sintéticos.

---

## Próximo documento

➡️ **02 - Arquitetura do Sistema**

Este documento apresenta o fluxo completo dos dados, desde a entrada das faturas até a atualização do Dashboard.