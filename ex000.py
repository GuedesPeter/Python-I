'''Crie um algoritmo que leia o nome de uma pessoa
e mostre uma mensagem de boasvindas
conforme o valor digitado'''

nome = input("Digite seu nome: ")
print("Olá", nome, ",prazer te conhecer!")


'''Crie um algoritmo python que leia o dia, o mês e o ano de nascimento
de uma pessoa e mostre uma mensagem com a data formatada'''

dia = int(input('Digite o dia do seu nacimento: '))
mes = int(input('Digite o mês do seu nacimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
print('Data de nascimento: {}/{}/{}.'.format(dia,mes,ano))

'''Crie um algoritmo que leia dois números e mostre
a soma entre eles'''
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = (num1 + num2)
print('A soma de {} + {} é igual a {}.'.format(num1,num2,soma))