'''
Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista
á na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
'''

lista_valores = []
for l in range(0,5):
    valor = int(input("Digite um valor: "))
    if l == 0 or valor > lista_valores[-1]:
        lista_valores.append(valor)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista_valores):
            if valor <= lista_valores[pos]:
                lista_valores.insert(pos,valor)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('--'*30)
print(lista_valores)




