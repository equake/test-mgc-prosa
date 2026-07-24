# AGENTS.md — Diretrizes de Codificação

## Geral

- **Linguagem:** Português — toda comunicação, comentários (quando explícitos pedidos) e documentação devem ser em português.
- **Sem comentários no código** — a menos que o usuário peça explicitamente. O código deve ser autoexplicativo.
- **KISS** — prefira soluções simples e diretas. Evite abstrações desnecessárias.
- **DRY** — não repita código. Extraia lógica comum em funções.
- **SOLID** — respeite os princípios de design, especialmente SRP e DIP.

## Python 3.10+

- Use **type hints** em todas as funções, parâmetros e retornos.
- Prefira `match ... case` (Python 3.10+) para múltiplas condições sobre a mesma variável.
- Use `typing.Annotated` e `typing.NewType` quando fizer sentido.
- Sempre use **PEP 8** como guia de estilo.
- Nomeclatura: `snake_case` para funções/variáveis, `PascalCase` para classes, `UPPER_CASE` para constantes.
- Use f-strings para interpolação de strings.
- Prefira pathlibs (`pathlib.Path`) ao invés de `os.path`.
- Use `if __name__ == "__main__":` apenas para scripts executáveis, não para módulos importados.
- Evite `import *` — sempre importe explicitamente.
- Agrupe imports: builtins, externos, locais, separados por linha em branco.

## FastAPI

- Use **Pydantic v2** models (`BaseModel`, `field_validator`, etc.) para validação de entrada/saída.
- Todas as rotas devem ter **response_model** definido.
- Estrutura modular:
  - `app/models/` — schemas Pydantic
  - `app/services/` — lógica de negócio
  - `app/routes/` — endpoints
  - `app/exceptions/` — exceções customizadas
- Use `APIRouter` para organizar rotas por domínio.
- Trate erros com `HTTPException` ou exceções customizadas + exception handlers no `main.py`.
- Use `Depends` para injeção de dependências quando fizer sentido (DB sessions, configs).
- Validações complexas devem ficar nos models (Pydantic) ou services — nunca nas routes.
- Endpoints públicos devem ter `tags` no router para documentação Swagger.

## Testes

- Use `pytest` como framework de testes.
- Use `httpx` para testes de integração com FastAPI (`ASGITransport`).
- Use `pytest-asyncio` para testes assíncronos.
- Nomeie os arquivos como `test_<modulo>.py`.
- Agrupe testes relacionados em classes com prefixo `Test`.
- Nomeie os testes com `test_<acao>_<condicao>_<resultado>`.
- Mantenha testes independentes e determinísticos.
- Use fixtures (`@pytest.fixture`) para setup reutilizável.
- Antes de qualquer merge ou entrega, **os testes devem passar**: `pytest tests/ -v`.

## Git

- Commits concisos, em português, seguindo Convention:
  - `feat: descrição` — nova funcionalidade
  - `fix: descrição` — correção de bug
  - `refactor: descrição` — refatoração
  - `test: descrição` — testes
  - `docs: descrição` — documentação
- Nunca comita credenciais, `.env`, `__pycache__`, `venv/`, `.pytest_cache/`.

## Estrutura do Projeto

```
project/
├── main.py                # Entry point FastAPI
├── requirements.txt       # Dependências
├── AGENTS.md              # Diretrizes (este arquivo)
├── README.md              # Documentação
├── app/
│   ├── __init__.py
│   ├── models/            # Schemas Pydantic
│   ├── services/          # Lógica de negócio
│   ├── routes/            # Endpoints
│   └── exceptions/        # Exceções customizadas
└── tests/
    ├── __init__.py
    ├── test_<service>.py  # Unitários
    ├── test_<models>.py   # Schemas
    └── test_<route>.py    # Integração
```
