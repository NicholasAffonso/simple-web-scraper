from bs4 import BeautifulSoup
import requests

# === Requests === #

header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'} # Simula um navegador

font = requests.get('https://g1.globo.com/', headers = header) # Pede o conteúdo RAW da página informando o cabeçalho

content = font.text # Armazena o conteúdo convertendo em texto (string)

# === BeautifulSoup === #

site = BeautifulSoup(content,'html.parser') # Cria estrutura html

news = site.find_all('div', class_='feed-post-body')

new = news[0]

for new in news:
    for new in new:
        print(new.get_text())
        

# === Retorno === #
print('\n', site.title.string)
print('', len(news), 'Notícias encontradas')
print(' cada notícia contém {} elementos'.format(len(new)))