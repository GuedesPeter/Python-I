

'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.

'''


num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} Convertido para Binério é igual a {}.'.format(num,bin(num)[2:]))
elif opcao == 2:
    print("{} Convertido para Octal é igual a {}.".format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {}.'.format(num,hex(num)[2:]))
else:
    print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")




'''
b = bin(num)
o = oct(num)
hex = hex(num)

print('Binério de {} = {}'.format(num,b))
print('Octal de {} = {}'.format(num,o))
print('Hexadecimal de {} = {}'.format(num,hex))

'''
