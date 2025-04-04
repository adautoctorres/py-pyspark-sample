# Configuração do Projeto com Poetry

Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciamento de dependências e ambiente virtual. Abaixo estão os comandos básicos para configurar o projeto.

## Inicializar o Projeto
```bash
poetry init
```
Siga as instruções para configurar o `pyproject.toml`.

## Instalar Dependências
Para instalar as dependências definidas no projeto:
```bash
poetry install
```

## Adicionar Dependências
Para adicionar uma dependência ao projeto:
```bash
poetry add <nome-da-dependencia>
```

Para adicionar uma dependência de desenvolvimento:
```bash
poetry add --dev <nome-da-dependencia>
```

### Adicionar o PySpark
Para adicionar o PySpark como dependência ao projeto:
```bash
poetry add pyspark
```

## Ativar o Ambiente Virtual
Para ativar o ambiente virtual gerenciado pelo Poetry:
```bash
poetry shell
```

## Executar Scripts
Para executar scripts Python no ambiente virtual sem ativá-lo:
```bash
poetry run python <script.py>
```

## Atualizar Dependências
Para atualizar todas as dependências do projeto:
```bash
poetry update
```

## Publicar o Projeto
Para publicar o projeto em um repositório como o PyPI:
```bash
poetry publish --build
```

Consulte a [documentação oficial do Poetry](https://python-poetry.org/docs/) para mais detalhes.