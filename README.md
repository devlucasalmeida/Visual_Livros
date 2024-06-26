# Gerador de Página Web para Dados de Livros

Este programa em Python gera uma página da web exibindo dados de dois arquivos CSV localizados na pasta "datasets". Ele requer três bibliotecas: Streamlit, Pandas e Plotly. Siga estes passos para executar o programa:

## Requisitos de Instalação:

Certifique-se de ter o Python instalado no seu sistema.

Instale as bibliotecas necessárias usando o pip:

```
pip install streamlit pandas plotly
```

## Executando o Programa:

1. Navegue até o diretório que contém o arquivo runner.py.

2. Execute runner.py para iniciar o servidor local:
```
python runner.py
```
Isso abrirá um servidor em localhost.

## Páginas da Web:
### Página de Livros ("books"):
Exibe um resumo de todos os livros.

Possui um filtro pesquisável por faixa de valor dos livros.

Inclui uma tabela listando todos os livros.

Apresenta quatro gráficos:
  1. Gráfico de barras mostrando as datas de publicação dos livros por ano.
  2. Histograma mostrando os valores dos livros em incrementos de $5.
  3. Histograma mostrando as notas dos livros em incrementos de 0.1.
  4. Gráfico de barras mostrando a contagem dos gêneros mais escritos.
### Página de Revisão ("review"):
Permite a seleção de um livro para visualizar informações detalhadas.

Exibe gênero, valor, nota, data de publicação e avaliações individuais do livro selecionado.

## Estrutura de Arquivos:
datasets/: Contém os arquivos CSV com os dados dos livros utilizados pelo programa.

## Observações:
Verifique se os arquivos CSV na pasta "datasets" estão corretamente formatados e acessíveis para o programa.
