# Contribuindo

Agradecemos o interesse em contribuir! Siga estas diretrizes para manter a qualidade do projeto.

## Como Contribuir

1. **Fork** este repositório.
2. Crie uma branch a partir de `main`: `git checkout -b nome-da-feature`
3. Faça suas alterações e execute os testes: `pytest tests/ -v`
4. Commit suas mudanças: `git commit -m "feat: descrição da mudança"`
5. Push para a branch: `git push origin nome-da-feature`
6. Abra um Pull Request descrevendo suas alterações.

## Diretrizes de Code Review

- Codifique seguindo as diretrizes em [AGENTS.md](AGENTS.md).
- Use type hints em Python.
- Escreva testes para novas funcionalidades.
- Mantenha o código simples e legível.

## commits

Siga o Convention Commit:

| Prefixo       | Descrição                     |
|---------------|-------------------------------|
| `feat:`       | Nova funcionalidade           |
| `fix:`        | Correção de bug               |
| `refactor:`   | Refatoração de código         |
| `test:`       | Adição ou alteração de testes |
| `docs:`       | Mudanças na documentação      |

## Dúvidas

Abra uma issue descrevendo sua dúvidas ou sugestões.
