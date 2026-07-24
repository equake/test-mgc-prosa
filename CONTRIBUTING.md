# Guia de Contribuição

## Como Contribuir

### 1. Faça um Fork do Projeto

Clique no botão **Fork** no canto superior direito do repositório.

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/test-mgc-prosa.git
cd test-mgc-prosa
```

### 3. Crie uma Branch

```bash
git checkout -b nome-da-sua-feature
```

### 4. Faça suas Alterações

Siga as diretrizes de codificação definidas em [AGENTS.md](AGENTS.md).

### 5. Execute os Testes

Certifique-se de que todos os testes passam antes de enviar suas alterações:

```bash
pytest tests/ -v
```

### 6. Commite suas Alterações

Utilize mensagens concisas seguindo Convention Commit:

- `feat: descrição` — nova funcionalidade
- `fix: descrição` — correção de bug
- `refactor: descrição` — refatoração
- `test: descrição` — testes
- `docs: descrição` — documentação

### 7. Envie para o Seu Fork

```bash
git push origin nome-da-sua-feature
```

### 8. Abra um Pull Request

Crie um PR descrevendo claramente as alterações realizadas.

## Diretrizes de Código

Consulte [AGENTS.md](AGENTS.md) para diretrizes completas de codificação, incluindo convenções de Python, FastAPI e testes.

## Estrutura do Projeto

```
project/
├── main.py                # Entry point FastAPI
├── requirements.txt       # Dependências
├── app/
│   ├── models/            # Schemas Pydantic
│   ├── services/          # Lógica de negócio
│   ├── routes/            # Endpoints
│   └── exceptions/        # Exceções customizadas
└── tests/
```
