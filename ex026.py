



'''Faça um programa que leia uma frase pelo teclado
 e mostre quantas vezes aparece a letra “A”,em que posição ela aparece
 a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes nesta frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))




'''Usando .find() para achar a letra A na 1° posição e
coloquei + 1 para não retornar zero como posição

E usei o .rfind() para procurar da direita para a esquerda
pegando assim a ultima posição como requisitado

e coloquei o +1 para não retornar zero como posiçao'''
