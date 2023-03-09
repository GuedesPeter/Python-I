'''Crie um programa que leia quanto dineiro uma pessoa tem
na carteira e mostre quantos dolares ela pode comprar.
considere o dólar US$3.27'''

real = float(input('Qual o seu saldo na carteira? R$ '))
dolar = real / 5.15
print('Você possui R${} Reais e pode comprar US${:.2f} Dólares.'.format(real,dolar))