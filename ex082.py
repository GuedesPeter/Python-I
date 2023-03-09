

'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.

'''

lista = []
pares = []
impares = []

while True:
    valor = int(input('Digite o valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    if continuar in 'N':
        break



print('--'*30)
print(f'A Lista completa é: {lista}')
print('--'*30)
print(f'Lista dos números PARES: {pares}')
print('--'*30)
print(f'Lista dos números ÍMPARES: {impares}')
print('--'*30)

