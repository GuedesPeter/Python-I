

'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

#MINHA SOLUÇÃO:

lista_peso = []
contador = 0
for contador in range(1,6):
    peso = float(input('Peso da {}° pessoa: Kg'.format(contador)))
    contador += 1
    lista_peso.append(peso)
print('FORAM INSERIDOS {} PESOS : '.format(contador-1))
print('\033[33mO MENOR peso entre todos digitados é {:.1f}Kg.'.format(min(lista_peso)))
print('\033[31mO MAIOR peso  entre todos digitados é {:.1f}Kg.'.format(max(lista_peso)))





#SOLUÇÃO DO VÍDEO:

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}KG.'.format(maior))
print('O menor peso lido foi de {}KG.'.format(menor))

    



