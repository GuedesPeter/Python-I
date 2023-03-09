
'''
Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.

'''

lista_valores = []
maior = 0
menor = 0
for c in range(0,5):
     lista_valores.append(int(input(f'Digite um valor para a posição {c}: ')))
     if c == 0:
         maior = lista_valores[c]
         menor = lista_valores[c]

     else:
        if lista_valores[c] > maior:
            maior = lista_valores[c]
        if lista_valores[c] < menor:
            menor = lista_valores[c]
print('--'*30)
print(lista_valores)
print(f'O maior valor digitado foi {maior} na posição : ',end='')
for indice,valor in enumerate(lista_valores):
    if valor == maior:
        print(f'{indice}...',end='')
print()
print(f'O menor valor digitado foi {menor} na posição : ',end='')
for indice,valor in enumerate(lista_valores):
    if valor == menor:
        print(f'{indice}...',end='')
print()



