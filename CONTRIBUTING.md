# Contribuindo

Obrigado pelo interesse em contribuir com este projeto! Siga as instruções abaixo para tornar o processo simples e eficiente.

## Como Contribuir

### 1. Faça um Fork

Clique no botão **Fork** no canto superior direito do repositório para criar sua cópia.

### 2. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/test-mgc-prosa.git
cd test-mgc-prosa
```

### 3. Crie um Branch

```bash
git checkout -b nome-do-branch
```

Use nomes descritivos:
- `feat/nome-da-funcionalidade`
- `fix/descricao-do-bug`
- `refator/nome-da-refatoracao`

### 4. Instale as Dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Desenvolva e Teste

Siga as diretrizes de código em [AGENTS.md](AGENTS.md).

Execute os testes antes de enviar:

```bash
pytest tests/ -v
```

Todos os testes devem passar.

### 6. Commits

Siga a convenção de commits:

```
tipo: descricao curta

- feat: nova funcionalidade
- fix: correção de bug
- refactor: refatoração
- test: testes
- docs: documentação
```

### 7. Envie um Pull Request

1. Faça push do seu branch:

```bash
git push origin nome-do-branch
```

2. Abra um PR no GitHub com:
   - Título claro e descritivo
   - Descrição das mudanças
   - Referencia a issue relacionada, se houver

## Diretrizes de Código

Consulte [AGENTS.md](AGENTS.md) para as diretrizes completas de codificação, incluindo convenções de Python, FastAPI e testes.

## Dúvidas

Abra uma issue para discutir mudanças significativas antes de implementá-las.
