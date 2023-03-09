

'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.

'''


lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    continuar = input('Quer continuar [S/N] ?').strip().upper()[0]
    if continuar in 'N':
        print('--'*30)
        break

print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontado na lista.')
