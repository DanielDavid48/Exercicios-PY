import urllib
from urllib.request import urlopen

def conecta_site():

    try:
        site = input('Digite qual é o site com https, http, www. e .com e;ou .br: ')
        site = urlopen(f'{site}')
    except urllib.error.URLError:
        print(f'o site do {site} não está acessível no momento')
    else:
        print(f'consegui acessar o site do {site}')
conecta_site()