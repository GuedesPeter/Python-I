

'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.

'''

lista = [[],[]]

for l in range(0,7):
    num = int(input(f'Digite o {l+1}° número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'PARES: {sorted(lista[0])}')
print(f'ÍMPARES: {sorted(lista[1])}')



