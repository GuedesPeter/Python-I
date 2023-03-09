

'''
Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''



print('GERADOR DE PA')
print('--'*30)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais #Inicia já com o total valendo 10
    while contador <= total:
        print('{} >> '.format(termo),end='')
        termo += razao
        contador +=1
    print('PAUSA')
    print('--'*30)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Aritmética finalizada com {} termos mostrados.'.format(total))

