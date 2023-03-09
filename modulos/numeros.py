
'''
              Modularização em Python

Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo como criar módulos em Python
e reutilizar nossos códigos em outros projetos.
Vamos aprender também como agrupar vários módulos em um pacote,
ampliando ainda mais a modularização em grandes projetos em Python.


def fatorial(n):
    f = 1
    for c in range(1,n +1):
        f *= c
    return f


num  =  int(input('Digite um valor:'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
----------------------------------------------- --------------------
PARA O PYTHON TODO ARQUIVO (.PY) PODE SER UM MÓDULO DESDE QUE POSSUA
FUNÇÕES (DEF) INTERNAS


>>> VANTAGENS:

- ORGANIZAÇÃO DO CÓDIGO : QUANDO MODULARIZA DIVIDE-SE O CÓDIGO
EM PARTES MENORES, POSSIBILITANDO FACILIDADE DE ACESSO A UMA
DETERMINADA PERTE ESCOLHIDA;

- FACILITA MANUTENÇÃO: CASO ALGO PARE DE FUNCIONAR OU HAJA MELHORIAS
A SEREM FEITAS NO CÓDIGO,TBM É FACILITADO O ACESSO PODENDO CORRIGIR
O ERRO OU ALTERAR A FUNÇÃO ESCOLHIDA;

- OCULTAÇÃO DO CÓDIGO DETALHADO: NÃO PRECISO ME PREOCUPRA COM AS
DETERMINADAS PARTES DO CÓDIGO,E SIM APENAS SABER O QUE AS FUNÇÕES
DO MODULO CRIADO FAZEM;

- REUTILIZAÇÃO: POSSO REUTILIZAR MEUS MÓDULOS EM OUTROS PROJETOS
(CÓDIGOS),É SÓ COPIAR O ARQUIVO COM O MÓDULO PARA A PASTA DO PROJETO
DESEJADO E REALIZAR A IMPORTAÇÃO;



>>> PACOTES (BIBLIOTECAS) <<<

É A JUNÇÃO DE MÓDULOS SEPARADOS POR ASSUNTOS,NADA MAIS É DO QUE
UMA PASTA QUE CONTÉM MÓDULOS.

DENTRO DO MEU "PACOTE ÚTEIS" POSSO TER DIVERSOS MÓDULOS PARA
TRATAMENTO DE NÚMEROS,STRINGS,DATAS,CORES,ETC.

NO PACOTE A IMPORTAÇÃO OCORRE DA MESMA MANEIRA:
- IMPORT UTEIS
- FROM UTEIS IMPORT DATAS
- FROM UTEIS IMPORT NUMEROS,STRINGS


DENTRO DE UM PROJETO PYTHON TODA PASTA É CONSIDERADA UM PACOTE
DENTRO DE CADA UMA DAS PASTAS DEVE CONTER UM ARQUIVO __INIT__.PY
EX:
PASTA(UTEIS)
__INIT__.PY
    -PASTA(CORES)
    __INIT__.PY
    -PASTA(DATAS)
    __INIT__.PY
    -PASTA(NUMEROS)
    __INIT__.PY
    -PASTA(STRINGS)
    __INIT__.PY

PACOTES SERÃO UTILIZADOS QUANDO OS PROGRAMAS FICAREM EXCESSIVAMENTE
GRANDES,DO CONTRÁRIO OS MÓDULOS DARÃO CONTA DO RECADO





'''




from uteis import numeros
num  =  int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}.')
print(f'O Dobro de {num} é {numeros.dobro(num)}.')
print(f'O Triplo de {num} é {numeros.triplo(num)}.')

