# API Validação de CNPJ

API REST para validação de CNPJ, construída com FastAPI. Validação offline utilizando o algoritmo de dígitos verificadores da Receita Federal.

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

**Códigos de status:**

| Código | Descrição |
|---|---|
| `200` | Processado com sucesso (válido ou inválido) |
| `422` |Payload inválido (campo ausente ou CNPJ com menos de 14 dígitos) |
| `405` | Método HTTP não permitido |

## Testes

```bash
pytest tests/ -v
```

## Exemplo com cURL

```bash
curl -X POST http://localhost:8000/cnpj/validate \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "11.222.333/0001-81"}'
```

## Estrutura do Projeto

```
test-mgc/
├── main.py                  # Entry point FastAPI
├── requirements.txt         # Dependências
├── app/
│   ├── models/
│   │   └── cnpj.py          # Schemas Pydantic (request/response)
│   ├── services/
│   │   └── cnpj_service.py  # Algoritmo de validação do CNPJ
│   └── routes/
│       └── cnpj.py          # Endpoint POST /cnpj/validate
└── tests/
    ├── test_cnpj_service.py # Testes unitários do algoritmo
    ├── test_cnpj_models.py  # Testes dos schemas Pydantic
    └── test_cnpj_routes.py  # Testes de integração da API
```

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — framework web
- [Pydantic](https://docs.pydantic.dev/) — validação de dados
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI
- [pytest](https://docs.pytest.org/) — testes
