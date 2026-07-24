# Guia de Contribuição

Obrigado pelo interesse em contribuir! Siga estas diretrizes para ajudar o projeto.

## Como Contribuir

### Relatando Bugs
1. Verifique se o bug já foi relatado nos issues.
2. Se for um bug novo, abra um issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. real
   - Versão do software e ambiente

### Sugestões de Melhorias
1. Abra um issue descrevendo a sugestão.
2. Explique o problema que a melhoria resolve.
3. Discuta a implementação com os mantenedores antes de codificar.

### Enviando Código

#### Preparação
```bash
# Fork e clone o repositório
git clone https://github.com/seu-usuario/repo.git
cd repo

# Crie um branch para sua contribuição
git checkout -b nome-da-feature

# Instale dependências
pip install -r requirements.txt
```

#### Desenvolvimento
- Siga as diretrizes em [AGENTS.md](AGENTS.md)
- Escreva testes para novas funcionalidades
- Mantenha a cobertura de testes

#### Pré-envio
```bash
# Execute os testes
pytest tests/ -v

# Formate o código
ruff format .
```

#### Commit e Pull Request
- Commits em português, seguindo Convention Commits:
  - `feat: nova funcionalidade`
  - `fix: correção de bug`
  - `refactor: refatoração`
  - `test: testes`
- Abra um PR com descrição clara das mudanças
- Aguarde revisão dos mantenedores

## Código de Conduta
Seja respeitoso e construtivo nas interações.
