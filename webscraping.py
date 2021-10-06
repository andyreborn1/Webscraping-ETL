#Instala as bibliotecas necesárias, caso não estejam instaladas
!pip install requests bs4

import requests
from bs4 import BeautifulSoup as bs

#Função para salvamento o arquivo
def download_file(url,filename):
  file_link = requests.get(url)

  
  with open(filename, 'wb') as fd:
    for chunk in file_link.iter_content(chunk_size=8192):
        fd.write(chunk)
        
