# Contribuindo

Agradecemos o interesse em contribuir com este projeto! Siga as instruções abaixo.

## Como Contribuir

### 1. Faça um Fork do Repositório

Clique em **Fork** no canto superior direito desta página para criar sua cópia do repositório.

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/test-mgc-prosa.git
cd test-mgc-prosa
```

### 3. Crie uma Branch

```bash
git checkout -b nome-da-sua-feature
```

### 4. Instale as Dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Faça Suas Alterações

Siga as diretrizes de codificação definidas em [AGENTS.md](./AGENTS.md).

### 6. Execute os Testes

```bash
pytest tests/ -v
```

Certifique-se de que todos os testes passam antes de enviar suas alterações.

### 7. Commit e Push

Siga a convenção de commits:

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `refactor:` refatoração
- `test:` testes
- `docs:` documentação

```bash
git add .
git commit -m "feat:descrição da sua alteração"
git push origin nome-da-sua-feature
```

### 8. Abra um Pull Request

No GitHub, clique em **Compare & pull request** para submeter suas alterações para revisão.

## Diretrizes

- Siga o estilo de código definido em [AGENTS.md](./AGENTS.md)
- Escreva testes para nova funcionalidade
- Mantenha os commits focados e bem descritos
- Não envie credenciais, `.env`, `__pycache__`, `venv/` ou `.pytest_cache/`

## Dúvidas

Abra uma [issue](https://github.com/equake/test-mgc-prosa/issues) para discutir mudanças ou tirar dúvidas.
