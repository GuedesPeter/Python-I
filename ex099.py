

'''
 Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores
 e dizer qual deles é o maior.

'''
#MINHA SOLUÇÃO
def maior(*num):
    valor = num
    print(valor)
    print(f'O maior valor encontrado é {max(valor)} .')


#PROGRAMA PRINCIPAL

maior(2,4,6,8,22,3,1,6,0,2,4)
print('-'*30)
maior(1,2,3,4,5,6,7,8,9,10)
print('-'*30)

#SOLUÇÃO CURSO EM VIDEO

from time import sleep
def mais(*num):
    cont = 0
    maior = 0
    print("\nAnalisando valores...")
    for valor in num:
        print(f'{valor}')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior} .')

#PROGRAMA PRINCIPAL

mais(4,7,0)
mais(2,3,7,9,50,66,1)
