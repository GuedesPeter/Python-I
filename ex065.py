

'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
'''

resposta = 's'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar [S/N] ?')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant,media))
print('O maior valor foi {} - O menor valor foi {}.'.format(maior,menor))

