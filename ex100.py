

'''
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia():
    for valor in range(0,5):
        num = randint(1,10)
        numeros.append(num)
    print(numeros)



def somaPar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares da lista é {soma} . ')


#PROGRAMA PRINCIPAL --------------------------------------------

numeros = []
sorteia()
somaPar()

 
































'''

def sorteia(lista):
    for valor in range(0,5):
        num = randint(1,10)
        lista.append(num)
    print(numeros)





def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')










numeros = []
sorteia()
somaPar()
'''
