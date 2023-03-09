


'''
Faça um programa que
calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.

'''

soma = 0
cont = 0
for multiplo in range(1,501,2):
    if multiplo % 3 == 0:
        cont = cont + 1
        soma = soma + multiplo
print('''A soma dos {} múltiplos de 3 no intervalo entre 1 e 500 é
{}.'''.format(cont,soma))
