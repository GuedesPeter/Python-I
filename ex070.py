

'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.

'''
soma = 0
maior = 0
menor = 0
contador = 0
mais_barato = 0
while True:
    nome = input('Nome do produto: ')
    valor = float(input('Preço: R$ '))
    contador += 1
    soma += valor
    if valor > 1000:
        maior += 1
    #OBTENDO MENOR VALOR E O NOME DO PRODUTO
    if contador == 1:
        menor = valor
        mais_barato = nome
    else:
        if valor < menor:
            menor = valor
    continuar = input('Você quer continuar [S/N]? ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Você quer continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^}'.format(' FINALIZADO.'))
print(f'{maior} Produtos custam mais de R$1000.00')
print(f'O produto mais barato é  {mais_barato} e custa R${menor} .')


