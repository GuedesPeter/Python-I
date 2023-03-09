'''Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço,com 5% de desconto'''

valor = float(input('Valor do produto: R$'))
novo_valor = valor-(valor*5/100)
print('O produto custa R${:.2f} , e com o desconto de 5% custará R${:.2f}.'.format(valor,novo_valor))