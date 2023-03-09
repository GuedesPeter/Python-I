

'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.

'''


produtos = ("COCA-COLA",9.95,"CHOCOLATE",7.75,"BOLACHA",5.65,"IOGURTE",4.25,"PIPOCA",3.05)

print('--'*20)
print('{LISTAGEM DE PREÇOS}')
print('--'*20)


for posicao,item in enumerate(produtos):
    if posicao %2 == 0:
        print(f'{produtos[posicao]:.<20}',end='')
    else:
        print(f'R$ {produtos[posicao]:>8.2f}')

