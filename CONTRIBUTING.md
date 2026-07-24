# Contribuindo

## Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/sua-feature`)
3. Faça commit das suas alterações (`git commit -m 'feat: descrição da feature'`)
4. Faça push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request

## Diretrizes de Commit

Siga a Convention Commits:
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `refactor:` refatoração
- `test:` testes
- `docs:` documentação

## Padrões de Código

- Siga as diretrizes em [AGENTS.md](./AGENTS.md)
- Python 3.10+ com type hints
- FastAPI com Pydantic v2
- Testes com pytest

## Dicas

- Antes de submeter, execute `pytest tests/ -v` para garantir que todos os testes passam
- Mantenha os commits concisos e em português
