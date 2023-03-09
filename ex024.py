'''Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome “SANTO”.'''

cidade = input('Digite o nome da cidade: ').strip()
#print('Existe o nome "SANTO" na cidade? {}'.format('santo'in cidade))
print(cidade[:5].upper() == 'SANTO')





