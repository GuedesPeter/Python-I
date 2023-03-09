'''MANIPULANDO TEXTOS'''
#VIDE CADERNO!

'''Nessa aula, vamos aprender operações com String no Python.
 As principais operações que vamos aprender são o Fatiamento de String,
 Análise com len(), count(), find(), transformações com 
 replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().'''

#FATIAMENTO

'''FATIAMENTO é pegar pedaços de uma string.
'''
frase = 'curso em video python'
#seleciona do caracter na posição 9 até a posição 14
print(frase[9:14])
#SEMPRE será IGNORADO a Ultima POSIÇÃO
print(frase[9:21])
#PULANDO POSIÇÕES - neste caso salta de 2 em 2
print(frase[9:21:2])
'''Colocando : sem numero antes [:5]-ANTES DOS : É ONDE ELE VAI COMEÇAR
DEPOIS DOS : É ONDE ELE VAI TERMINAR [:5]'''
print(frase[:5])

'''COLOCANDO O NUMERO DA POSIÇÃO ANTES E DEPOIS : - SIGNIFICA QUE
 EU INDIQUEI O INICIO MAS NÃO SEI O FINAL - [15:]
 FATIARÁ DA POSIÇÃO 15 ATÉ O FINAL'''
print(frase[15:])

'''COMEÇARÁ NA POSIÇÃO 9 E IRÁ ATÉ O FINAL PULANDO DE 3 EM 3
NESTE CASO [9::3'''
print(frase[9::3])

'''ANÁLISE DE STRING:'''

'''LEN() - RETORNARÁ O COMPRIMENTO DA STRING,LISTA,ETC.
,OU SEJA,O TAMANHO DELA'''
print(len(frase))

'''.COUNT - FARÁ COM QUE SEJA CONTADO A QUANTIDADE DE UM DETERMINADO
CARACTER EM UMA STRING,LISTA,ETC.'''
print(frase.count('o'))
#CONTAGEM COM FATIAMENTO - pegando da posição 0 até a 13
# e considerando quantos 'o' tem nesse intervalo
print(frase.count('o',0,13))

'''.FIND DIZ QUANTAS VEZES ELE 'ENCONTROU (FIND)' - DEO'''
print(frase.find('deo'))

'''QUANDO COLOCADO NO .FIND UMA STRING QUE NÃO EXISTE
ELE RETORNARÁ O VALOR -1'''
print(frase.find('android'))

'''O OPERADOR 'IN' É USADO PARA VERIFICAR - neste caso:
Existe 'CURSO' (in) dentro da variável FRASE?
CASO SIM RETORNA ->>> TRUE
CASO NÃO RETONA ->>> FALSE'''
print('curso' in frase)

"======================================================================="
'''TRANSFORMAÇÃO DE STRING'''

'''.REPLACE() - IRÁ SUBTITUIR,OU TROCAR UMA COISA POR OUTRA
Neste caso substituirá a string: PYTHON pela string: ANDROID'''
print(frase.replace('python','android'))

'''.UPPER() - DEIXARÁ O CONTEÚDO TODO EM MAIÚSCULO,mantendo o que
já esta em maiúsculo'''
print(frase.upper())

'''.LOWER() - DEIXARÁ TUDO EM MINÚSCULO,metodo contrário ao upper()'''
print(frase.lower())

'''.CAPTALIZE() - JOGARÁ TODOS OS CARACTERES PARA MINÚSCULO DEIXANDO
APENAS O PRIMEIRO CARACTER EM MAIÚSCULO'''
print(frase.capitalize())

'''.TITLE() - IRÁ ANALISAR OS CARACTERES PELA POSIÇÃO E DEIXARÁ
EM MAIÚSCULO A PRIMEIRA LETRA DE CADA PALAVRA EM MAIÚSCULO'''
print(frase.title())

frase1 = '   Aprenda Python   '

'''.STRIP - REMOVE ESPAÇOS EXCEDENTES NO INÍCIO E NO FINAL DA CADEIA'''
print(frase1.strip())

'''.RSTRIP - REMOVE ESPAÇOS EXCEDENTES  DA CADEIA
ALINHANDO OS CARACTERES A DIREITA
Neste caso remove somente os espaços do final'''
print(frase1.rstrip())

'''.LSTRIP - REMOVE ESPAÇOS EXCEDENTES  DA CADEIA
ALINHANDO OS CARACTERES A ESQUERDA
Neste caso remove somente os espaços do inicio'''
print(frase1.lstrip())

'======================================================================'

'''DIVIDIR STRINGS'''

'''.SPLIT - É FEITO EM SEUS ESPAÇOS,DIVIDIRÁ SUA STRING 
EM UMA LISTA E PEGARA OS
ESPAÇOS OS REPOSICIONANDO'''
# CURSO EM VIDEO PYTHON
# 01234 01 01234 012345
print(frase.split())

'''.JOIN - IRÁ JUNTAR TODOS OS ELEMENTOS E USARÁ O SEPARADOR (-)
GERANDO UMA STRING UNICA'''
print(' -'.join(frase))
















