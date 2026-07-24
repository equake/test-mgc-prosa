# Guia de Contribuição

Obrigado pelo interesse em contribuir com este projeto! Siga as instruções abaixo para facilitar o processo.

## Como Contribuir

### 1. Faça um fork do repositório

Clique em **Fork** no canto superior direito do repositório e clone sua cópia localmente:

```bash
git clone https://github.com/seu-username/test-mgc-prosa.git
cd test-mgc-prosa
```

### 2. Crie uma branch

Crie uma branch a partir de `main` com um nome descritivo:

```bash
git checkout -b feat/nome-da-funcionalidade
```

### 3. Desenvolva

Siga as diretrizes de codificação definidas em [AGENTS.md](./AGENTS.md). Resumindo:

- Use **Python 3.10+** com type hints em todas as funções.
- Siga **PEP 8** para estilo de código.
- Estrutura modular: `models/`, `services/`, `routes/`, `exceptions/`.
- Use **Pydantic v2** para schemas de validação.
- Nomeclatura: `snake_case` para funções/variáveis, `PascalCase` para classes.

### 4. Execute os testes

Antes de enviar sua contribuição, certifique-se de que todos os testes passam:

```bash
pytest tests/ -v
```

### 5. Commits

Siga a **Conventional Commits** em português:

- `feat: descrição` — nova funcionalidade
- `fix: descrição` — correção de bug
- `refactor: descrição` — refatoração
- `test: descrição` — testes
- `docs: descrição` — documentação

### 6. Envie um Pull Request

Abra um PR com:

- Título claro e descritivo.
- Descrição do que foi alterado e por quê.
- Referência à issue, se aplicável.
- Confirmação de que os testes passaram localmente.

## Regras Importantes

- Não comite credenciais, arquivos `.env`, `__pycache__`, `venv/` ou `.pytest_cache/`.
- Mantenha o código limpo, autoexplicativo e sem comentários desnecessários.
- PRs sem testes podem ser rejeitados.

## Dúvidas

Abra uma [issue](https://github.com/seu-username/test-mgc-prosa/issues) para discutir sua ideia antes de implementar.
