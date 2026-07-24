# API Validação de CNPJ e CPF

API REST para validação de CNPJ e CPF usando FastAPI e o algoritmo de dígitos verificadores da Receita Federal.

## Instalação

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Execução

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Swagger UI: `http://localhost:8000/docs`

## Endpoints

- `POST /cnpj/validate` — valida CNPJ
- `POST /cpf/validate` — valida CPF

## Testes

```bash
pytest tests/ -v
```

## Tecnologias

- FastAPI
- Pydantic v2
- Uvicorn
- pytest
