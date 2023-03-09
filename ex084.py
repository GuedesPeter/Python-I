

'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

'''

dados = []
nomepeso = []
maior = []
menor = []

while True:
    nomepeso.append(input('NOME: '))
    nomepeso.append(float(input('PESO: ')))
#----------- MAIOR E MENOR PESO --------------------------
    if len(dados) == 0:
        maior = nomepeso[1]
        menor = nomepeso[1]
    else:
        if nomepeso[1] > maior:
            maior = nomepeso[1]
        if nomepeso < menor:
            menor = nomepeso[1]
    dados.append(nomepeso[:])#Inserindo uma CÓPIA do conteúdo da lista nomepeso na lista dados
    nomepeso.clear() #APAGANDO o conteúdo da lista nomepeso para não gerar duplicidade na lista dados

    continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    if continuar in 'N':
        break
# -------------- PESADAS E LEVES --------------------------------
print('--'*30)
print(f'Foram cadastradas {len(dados)} pessoas.')
for p in dados:
    if p[1] == maior:
        print(f'Lista dos pesados: {p[0]}')

for p in dados:
    if p[1] == menor:
        print(f'Lista dos leves: {p[0]}')



