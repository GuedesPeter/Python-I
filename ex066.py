

'''
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados
e qual foi a soma entre elas (desconsiderando o flag).

'''

from time import sleep
contador = 0
soma = 0

while True:
    num = int(input('Digite um valor ou [999] para finalizar: '))
    if num == 999:
        break
    contador +=1
    soma = soma + num

sleep(1),print('FINALIZANDO...')
sleep(1.5),print(f'Você digitou {contador} números, e a soma entre eles é igual a {soma}.')

