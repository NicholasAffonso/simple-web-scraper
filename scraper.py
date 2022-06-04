from bs4 import BeautifulSoup
import requests

# === Requests === #

header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'} # Simula um navegador

font = requests.get('https://g1.globo.com/', headers = header) # Pede o conteúdo RAW da página informando o cabeçalho

content = font.text # Armazena o conteúdo convertendo em texto (string)

# === BeautifulSoup === #

site = BeautifulSoup(content,'html.parser') # Monta estrutura html

bnews = site.find_all('div', class_='bstn-hl')
news = site.find_all('div', class_='feed-post-body') # Busca e armazena tag div com classe específica


for new in news:

    header = new.find('span', {'class':'feed-post-header-chapeu'}).text
    title = new.find('a', {'class':'feed-post-link'}).text
    date = new.find('span', {'class':'feed-post-datetime'}).text
    meta = new.find('span', {'class':'feed-post-metadata-section'}).text

    print('\n{}\n{}\n{}\n{}\n'.format(header, title, date, meta))

for bnew in bnews:
    b_header = bnew.find('div', {'class':'bstn-headline-skeleton'})
    print('{}\n'.format(b_header))

    #print(bnews)


# === Retorno === #
print('\n', site.title.string)
print('', len(news), 'Notícias encontradas')