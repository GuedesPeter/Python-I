

'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.

'''

lista_valores = []

while True:
    valor = (int(input('Digite uma valor: ')))
    if valor not in lista_valores:
        lista_valores.append(valor)
    else:
        print('Valor duplicado não será adicionado.')
    continuar = str(input('Quer continuar [S/N] ?')).strip().upper()[0]
    if continuar in 'Nn':
        break


print(f'Você digitou os valores: {sorted(lista_valores)}')

