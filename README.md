
# API Validação de CNPJ e CPF

API REST para validação de CNPJ e CPF, construída com FastAPI. Validação offline utilizando o algoritmo de dígitos verificadores da Receita Federal.

## Requisitos

- Python 3.10+

## Instalação

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## Execução

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

O servidor inicia em `http://localhost:8000`. A documentação interativa (Swagger UI) está disponível em `http://localhost:8000/docs`.

## Endpoints

### POST /cnpj/validate

Valida um CNPJ e retorna se é válido ou não.

**Request:**

```json
{
  "cnpj": "11.222.333/0001-81"
}
```

O campo `cnpj` aceita:
- Dígitos puros: `11222333000181`
- Com máscara: `11.222.333/0001-81`
- Com espaços: `11 222 333 / 0001 - 81`

**Response (200):**

```json
{
  "valid": true,
  "cnpj": "11.222.333/0001-81",
  "message": "CNPJ válido"
}
```

### POST /cpf/validate

Valida um CPF e retorna se é válido ou não.

**Request:**

```json
{
  "cpf": "123.456.789-09"
}
```

O campo `cpf` aceita:
- Dígitos puros: `12345678909`
- Com máscara: `123.456.789-09`
- Com espaços: `123 456 789 09`

**Response (200):**

```json
{
  "valid": true,
  "cpf": "123.456.789-09",
  "message": "CPF válido"
}
```

### Códigos de status

| Código | Descrição |
|---|---|
| `200` | Processado com sucesso (válido ou inválido) |
| `422` | Payload inválido (campo ausente ou tamanho incorreto) |
| `405` | Método HTTP não permitido |

## Testes

```bash
pytest tests/ -v
```

## Exemplo com cURL

```bash
# Validar CNPJ
curl -X POST http://localhost:8000/cnpj/validate \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "11.222.333/0001-81"}'

# Validar CPF
curl -X POST http://localhost:8000/cpf/validate \
  -H "Content-Type: application/json" \
  -d '{"cpf": "123.456.789-09"}'
```

## Estrutura do Projeto

```
test-mgc/
├── main.py                  # Entry point FastAPI
├── requirements.txt         # Dependências
├── app/
│   ├── models/
│   │   ├── cnpj.py          # Schemas Pydantic (CNPJ)
│   │   └── cpf.py           # Schemas Pydantic (CPF)
│   ├── services/
│   │   ├── cnpj_service.py  # Algoritmo de validação do CNPJ
│   │   └── cpf_service.py   # Algoritmo de validação do CPF
│   └── routes/
│       ├── cnpj.py          # Endpoint POST /cnpj/validate
│       └── cpf.py           # Endpoint POST /cpf/validate
└── tests/
    ├── test_cnpj_service.py # Testes unitários do algoritmo CNPJ
    ├── test_cnpj_models.py  # Testes dos schemas Pydantic CNPJ
    ├── test_cnpj_routes.py  # Testes de integração da API CNPJ
    ├── test_cpf_service.py  # Testes unitários do algoritmo CPF
    ├── test_cpf_models.py   # Testes dos schemas Pydantic CPF
    └── test_cpf_routes.py   # Testes de integração da API CPF
```

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — framework web
- [Pydantic](https://docs.pydantic.dev/) — validação de dados
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI
- [pytest](https://docs.pytest.org/) — testes

## Integração com OpenCode (GitHub Actions)

Este repositório usa o bot [OpenCode](https://opencode.ai/) via GitHub Actions. Para acionar o bot em qualquer issue ou PR, comente `/oc` (ou `/opencode`) seguido da instrução desejada.

### Manejos necessários para criar Pull Requests via comentário

A integração passa por três adaptações necessárias para o cenário atual:

1. **Token `GITHUB_TOKEN` do runner nao cria PRs.** O token padrao do GitHub Actions nao tem permissao para chamar `POST /repos/{owner}/{repo}/pulls` em eventos de `issue_comment`, independentemente das permissoes declaradas em `permissions:`. **Solucao adotada:** usar um Personal Access Token (PAT) com escopo `repo` armazenado como secret `OPENCODE_PAT_TOKEN`. O PAT e passado para o checkout e para o step do opencode, permitindo que o bot abra PRs.

2. **Formato do OIDC mudou em 2026-07-15.** O OpenCode consome o OIDC token do GitHub (`id-token: write`) para se autenticar com o GitHub App oficial. O novo formato do token (`repo:owner@id/repo@id:ref:...`) quebra o parser do OpenCode, gerando o erro `Failed to parse JSON → "p.rest"` que mascara a causa real. Issue upstream: [anomalyco/opencode#37823](https://github.com/anomalyco/opencode/issues/37823). PR com correcao: [anomalyco/opencode#37889](https://github.com/anomalyco/opencode/pull/37889). **Workaround adotado ate o merge:** o step `Configure git identity` configura manualmente o autor do commit, contornando a dependencia do OIDC para commits e pushes.

3. **Loop infinito de auto-trigger.** Como o PAT credita os comentarios do opencode ao proprio usuario (e nao a um bot), o filtro `github.event.sender.type != 'Bot'` nao pega as respostas automaticas do opencode. **Solucao adotada:** filtro adicional por conteudo - `!contains(github.event.comment.body, 'opencode.ai/s/')` - que detecta o link de sessao que so o opencode inclui nas respostas e ignora esses comentarios.

### Configuracao local

- Variavel `OPENCODE_MODEL` (repository variable) com o modelo a ser usado (ex.: `anthropic/claude-sonnet-4-20250514`).
- Secret `MGC_PROSA_API_KEY` (ou outro provider) com a chave de API do LLM.
- Secret `OPENCODE_PAT_TOKEN` com o Personal Access Token usado para checkout e para `GITHUB_TOKEN` no step do opencode.
