'''DESAFIO 01:
Crie um programa que leia dois números e mostre a soma entre eles'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} vale {} !'.format(n1, n2, soma))

'''DESAFIO 02:
Faça um programa que leia algo pelo teclado e seu tipo primitivo(int,float,bool-true/false,string) e todas as informações possiveis sobre ele.'''
n = input('Digite algo: ')
'''n = bool(input('Digite algo: ')
print(n) - com valor digitado = True / sem valor digitado-vazio = False'''
'''n = int(input('Digite algo: ')
print(n) = corresponde a um número INTEIRO'''
'''n = float(input('Digite algo: ')
print(n) = corresponde a um número REAL'''
'''n = input('Digite algo: ')
print(n) = corresponde a uma STRING/caracter("str")'''

# Se n é do tipo número
print(n.isnumeric)
# Se n é do tipo alfabeto
print(n.isalpha)
# Se n é do tipo alfanumérico
print(n.isalnum)
# Se n é do tipo letra maiúscula
print(n.isupper)
# Se n é do tipo decimal
print(n.isdecimal)
# ENTRE OUTROS...