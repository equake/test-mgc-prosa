# Contribuindo

Agradecemos seu interesse em contribuir para este projeto!

## Como Contribuir

### Reportando Bugs

1. Verifique se o bug já foi reportado nos [Issues](../../issues).
2. Se não, abra um novo issue com:
   - Título descritivo
   - Passos para reproduzir
   - Comportamento esperado vs. real
   - Versões do software e ambiente

### Sugestão de Melhorias

- Abra um issue com a tag `enhancement` descrevendo a proposta.

### Enviando Código

1. Faça fork do repositório.
2. Crie uma branch: `git checkout -b feat/sua-melhoria`
3. Faça suas alterações seguindo as diretrizes em [AGENTS.md](./AGENTS.md).
4. Certifique-se de que os testes passam: `pytest tests/ -v`
5. Envie os commits: `git commit -m "feat: descricao"`
6. Envie para o fork: `git push origin feat/sua-melhoria`
7. Abra um Pull Request.

## Diretrizes de Código

Consulte [AGENTS.md](./AGENTS.md) para diretrizes detalhadas de codificação, incluindo:
- Estilo Python (PEP 8, type hints, etc.)
- Estrutura FastAPI
- Convenções de teste

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto.
