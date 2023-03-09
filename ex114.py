

'''
Crie um código em Python
que teste se o site pudim está acessível pelo computador usado.

'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('ERRO!')
else:
    print('Tudo OK! Site acessado com sucesso.')
    print(site.read())#PARA LER O CONTEUDO HTML DO SITE

    

