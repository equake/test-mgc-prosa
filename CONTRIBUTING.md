# Contribuindo

Obrigado pelo interesse em contribuir com este projeto! Siga as orientações abaixo para facilitar a colaboração.

## Como Contribuir

### 1. Faça um Fork do Repositório

Clique no botão **Fork** no canto superior direito desta página para criar sua própria cópia do repositório.

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/test-mgc-prosa.git
cd test-mgc-prosa
```

### 3. Crie um Branch

Crie um branch para sua mudança a partir de `main`:

```bash
git checkout -b seu-branch
```

### 4. Instale as Dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Desenvolva e Teste

Siga as diretrizes de codificação definidas em [AGENTS.md](./AGENTS.md).

Execute os testes antes de enviar sua contribuição:

```bash
pytest tests/ -v
```

Todos os testes devem passar.

### 6. Commit ePush

Segu a convenção de commits:

```
feat: descrição da nova funcionalidade
fix: descrição da correção
refactor: descrição da refatoração
test: descrição das mudanças nos testes
docs: descrição das mudanças na documentação
```

```bash
git add .
git commit -m "tipo: descrição concisa"
git push origin seu-branch
```

### 7. Abra um Pull Request

No GitHub, clique em **Compare & pull request**. Descreva as mudanças realizadas e aguarde a revisão.

## Diretrizes de Codificação

Este projeto segue diretrizes definidas em [AGENTS.md](./AGENTS.md). Destaque:

- **Python 3.10+** com type hints em todas as funções
- **PEP 8** como estilo de código
- **FastAPI** + **Pydantic v2** para a API
- **pytest** para testes
- Código autoexplicativo, sem comentários desnecessários

## Dúvidas

Para dúvidas ou sugestões, abra uma [issue](../../issues).
