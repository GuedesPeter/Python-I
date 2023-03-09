'''Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário com 15% de aumento'''

nome = input('Nome do funcionário: ')
salario = float(input('Salario do funcionário : R$'))
novo_salario = salario + (salario*15/100)
print('{} ganhava R${:.2f} de salário. Com novo aumento de 15% passou a ganhar R${:.2f} de salário mensal.'.format(nome,salario,novo_salario))
