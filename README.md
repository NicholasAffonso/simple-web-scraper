Um programa que retorna as primeiras notícias do G1
---

Pequeno experimento de web scraping no python utilizando bibliotecas [Requests](https://realpython.com/python-requests/#the-response) e [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

### Requests
- Simula um navegador
- Pede o conteúdo RAW da página informando o cabeçalho
- Armazena o conteúdo convertendo em texto (string)

### BeautifulSoup
- Monta estrutura HTML
- Busca e armazena a informação desejada em um array
- Percorre o array tratando a informação
- Imprime o resultado

### Retorna o tamanho da primeira variável