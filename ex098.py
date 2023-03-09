

'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1

b) de 10 até 0, de 2 em 2

c) uma contagem personalizada

'''
from time import sleep

def contador(inicio,fim,passo):
    # AJUSTANDO CASO PASSO SEJA NEGATIVO OU ZERO
    if passo < 0:
        passo += 1
    if passo == 0:
        passo = 1
    print('-'*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2.5)

    #PARA INICIO MENOR QUE O FIM
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont += passo
        print('FIM')

    #PARA FIM MAIOR QUE O INICIO
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM')
    print('-' * 20)

#----PROGRAMA PRINCIPAL----
contador(1,10,1)
contador(10,0,2)
print('--'*20)
print('PERSONALIZE A CONTAGEM: ')
ini = int(input('INICIO: '))
final = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini,final,pas)
