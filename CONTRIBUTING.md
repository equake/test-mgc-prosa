# Guia de Contribuição

## Como Contribuir

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`).
3. Faça commit das suas mudanças (`git commit -m 'feat: adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/minha-feature`).
5. Abra um Pull Request.

## Padrões de Commit

Siga a Convention Commits:

- `feat:` nova funcionalidade
- `fix:` correção de bug
- `refactor:` refatoração de código
- `test:` testes
- `docs:` documentação

## Padrões de Código

- Python 3.10+ com type hints em todas as funções.
- Siga PEP 8 como guia de estilo.
- Prefira `snake_case` para funções e variáveis, `PascalCase` para classes.
- Use f-strings para interpolação de strings.
- Evite `import *` — importe explicitamente.

## Testes

- Use `pytest` como framework de testes.
- Execute os testes antes de abrir um PR: `pytest tests/ -v`.
- Nomeie os testes como `test_acao_condicao_resultado`.

## Pull Requests

- Descreva claramente as mudanças realizadas.
- Reference o issue relacionado.
- Mantenha os PRs focados e pequenos.
