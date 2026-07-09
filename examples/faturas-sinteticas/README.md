# Faturas Sintéticas para Teste do Extrator

Esta pasta contém faturas sintéticas criadas para demonstrar o funcionamento do extrator sem expor dados financeiros reais.

## Arquivos de entrada

```text
input/
├── 2026-01 - Fatura Nubank - Fred.csv
├── 2026-01 - Fatura Santander - Fred.pdf
├── 2026-02 - Fatura Nubank - Laura.csv
├── 2026-02 - Fatura Santander - Laura.pdf
├── 2026-03 - Fatura Nubank - Nosso.csv
└── 2026-03 - Fatura Santander - Nosso.pdf
```

## Como testar

Na raiz do repositório, execute:

```bash
python src/extrator_faturas_casal.py
```

Quando o script pedir a pasta de entrada, informe:

```text
examples/faturas-sinteticas/input
```

Quando pedir a pasta de saída, informe:

```text
examples/faturas-sinteticas/output
```

## Saída esperada

O extrator deve gerar uma planilha `.xlsx` para cada fatura processada.

Resultado esperado no teste validado:

| Arquivo de saída | Linhas esperadas | Responsável | Banco | Período | Total esperado |
|---|---:|---|---|---|---:|
| 2026-01 - Fatura Nubank - Fred - Movimentações.xlsx | 13 | FRED | NUBANK | 2026-01 | R$ 688,64 |
| 2026-01 - Fatura Santander - Fred - Movimentações.xlsx | 15 | FRED | SANTANDER | 2026-01 | R$ 1.513,95 |
| 2026-02 - Fatura Nubank - Laura - Movimentações.xlsx | 13 | LAURA | NUBANK | 2026-02 | R$ 833,62 |
| 2026-02 - Fatura Santander - Laura - Movimentações.xlsx | 15 | LAURA | SANTANDER | 2026-02 | R$ 1.786,45 |
| 2026-03 - Fatura Nubank - Nosso - Movimentações.xlsx | 13 | NOSSO | NUBANK | 2026-03 | R$ 543,69 |
| 2026-03 - Fatura Santander - Nosso - Movimentações.xlsx | 15 | NOSSO | SANTANDER | 2026-03 | R$ 1.241,45 |

## Observação

A pasta `output/` está vazia por padrão. Ela será preenchida ao executar o extrator.
