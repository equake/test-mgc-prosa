# Guia de Contribuição

Obrigado por contribuir com o projeto API Validação de CNPJ e CPF!

## Índice

- [Configuração do Ambiente](#configuração-do-ambiente)
- [Executando o Projeto](#executando-o-projeto)
- [Testes](#testes)
- [Lint e Formatação](#lint-e-formatação)
- [Padrões de Código](#padrões-de-código)
- [Pull Requests](#pull-requests)
- [Commits](#commits)

## Configuração do Ambiente

1. **Fork e clone o repositório:**

```bash
git clone https://github.com/seu-usuario/test-mgc-prosa.git
cd test-mgc-prosa
```

2. **Crie um ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
pip install -e ".[dev,test]"
```

## Executando o Projeto

### Servidor Local

```bash
uvicorn main:app --host 0.0.0 --port 8000 --reload
```

A API estará disponível em `http://localhost:8000`. A documentação Swagger em `http://localhost:8000/docs`.

### Docker

```bash
docker build -t test-mgc-prosa .
docker run -p 8000:8000 test-mgc-prosa
```

## Testes

Execute todos os testes:

```bash
pytest tests/ -v
```

Execute um teste específico:

```bash
pytest tests/test_cnpj_service.py -v
```

Execute testes com cobertura:

```bash
pytest tests/ -v --cov=app --cov-report=term-missing
```

## Lint e Formatação

O projeto usa **Ruff** para lint e formatação.

```bash
ruff check .
ruff format .
ruff check --fix .
```

## Padrões de Código

Consulte [AGENTS.md](./AGENTS.md) para diretrizes detalhadas de codificação:

- Python 3.10+ com type hints em todas as funções
- PEP 8 como guia de estilo
- FastAPI com Pydantic v2 para validação
- Estrutura modular: `app/models/`, `app/services/`, `app/routes/`
- Nomenclatura: `snake_case` para funções/variáveis, `PascalCase` para classes

## Pull Requests

1. Crie uma branch a partir de `main`: `git checkout -b feature/sua-feature`
2. Faça suas alterações e adicione testes
3. Execute `ruff format . && ruff check .` antes de submeter
4. Execute `pytest tests/ -v` para garantir que todos os testes passam
5. Crie um Pull Request com descrição clara das alterações

## Commits

Siga Conventional Commits em português:

- `feat: descrição` — nova funcionalidade
- `fix: descrição` — correção de bug
- `refactor: descrição` — refatoração
- `test: descrição` — testes
- `docs: descrição` — documentação
