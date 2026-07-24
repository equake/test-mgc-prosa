# Como Contribuir

## Pré-requisitos

- Python 3.10+
- pip ou poetry

## Instalação

Instale as dependências do projeto:

```bash
pip install -e ".[test,dev]"
```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://localhost:8000`.

## Testes

Execute os testes com pytest:

```bash
pytest tests/ -v
```

## Linting e Formatação

Verifique o código com ruff:

```bash
ruff check .
```

Formate o código automaticamente:

```bash
ruff format .
```

## Pull Requests

1. Crie uma branch a partir de `main`: `git checkout -b feat/minha-feature`
2. Faça suas alterações e adicione testes quando aplicável
3. Execute os testes e o lint antes de enviar: `pytest tests/ -v && ruff check .`
4. Commit usando mensagens no formato: `feat: descrição`, `fix: descrição`, etc.
5. Abra um PR com uma descrição clara das alterações
