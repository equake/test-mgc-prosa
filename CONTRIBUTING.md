# Contribuindo

Agradecemos seu interesse em contribuir com este projeto! Siga estas diretrizes para facilitar a colaboração.

## Como Contribuir

### Relatando Problemas

1. Verifique se o problema já não está sendo discutido nos [Issues](https://github.com/equake/test-mgc-prosa/issues).
2. Abra um novo issue com uma descrição clara e passos para reproduzir.

### Enviando Pull Requests

1. Faça um fork do repositório.
2. Crie uma branch para sua mudança:
   ```bash
   git checkout -b feat/descricao-da-mudanca
   ```
3. Faça as alterações no código.
4. Execute os testes para garantir que tudo funciona:
   ```bash
   pytest tests/ -v
   ```
5. Commit suas mudanças seguindo a convenção:
   ```
   feat: descrição da funcionalidade
   fix: descrição da correção
   refactor: descrição da refatoração
   test: descrição dos testes
   ```
6. Envie para o seu fork e abra um Pull Request para o repositório original.

## Diretrizes de Código

- **Python 3.10+** com type hints em todas as funções.
- Siga **PEP 8** para estilo de código.
- Use **snake_case** para funções/variáveis e **PascalCase** para classes.
- Prefira `pathlib.Path` ao invés de `os.path`.
- Use f-strings para interpolação de strings.
- Sem comentários no código, a menos que estritamente necessários — o código deve ser autoexplicativo.
- Siga os princípios **KISS**, **DRY** e **SOLID**.

### Estrutura do Projeto

- `app/models/` — schemas Pydantic
- `app/services/` — lógica de negócio
- `app/routes/` — endpoints
- `app/exceptions/` — exceções customizadas
- `tests/` — testes unitários e de integração

## Testes

Todos os testes devem passar antes de submeter um PR:

```bash
pytest tests/ -v
```
