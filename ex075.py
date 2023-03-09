

'''
Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

'''

valor = (int(input('VALORES: ')),int(input('VALORES: ')),int(input('VALORES: ')),int(input('VALORES: ')))
print(f'Você digitou os valores: {valor}')
print(f'A) O número 9 apareceu {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O valor 3 aparece a primeira vez digitado na posição {valor.index(3)+1}')
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
for n in valor:
    if n % 2 == 0:
        print(f'VALOR PAR: {n}')



