#Import das bibliotecas necessárias
import requests
from bs4 import BeautifulSoup as bs

#Função para salvamento o arquivo
def download_file(url,filename):
  file_link = requests.get(url)

  
  with open(filename, 'wb') as fd:
    for chunk in file_link.iter_content(chunk_size=8192):
        fd.write(chunk)
        

#Função para encontrar o arquivo na url especifícada
def find_file(url):
  #Transforma a pagina html em um arquivo do bs4
  soup = bs(requests.get(url).content,"html.parser")

  #Encontra o link para a página de download do arquivo
  download_page_link = soup.find('a',attrs={'class':'alert-link internal-link'})['href']
  
  #Encontra o link do arquivo
  soup = bs(requests.get(download_page_link).content,'html.parser')
  pdf_download_link = soup.find('table').find('a')['href']

  filename = pdf_download_link.split('/')[-1]

  download_file(pdf_download_link,filename)


if __name__ == "__main__":
  URL = 'https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'
  find_file(URL)