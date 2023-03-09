

'''
 Crie um programa que leia dois valores e mostre um menu na tela:
 [ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

'''
from time import sleep
#MINHA RESOLUÇÃO
print('''\033[3;31m
QUAL OPERAÇÃO DESEJA REALIZAR?
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
soma = 0
multiplicar = 0
maior = 0
novos_numeros = 0
sair = 0
while True:
    n1= int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    escolha = int(input('Escolha a operação a realizar: '))
    if escolha == 1:
        soma = n1 + n2
        print('Você somou os valores {} e {} , obtendo {}.'.format(n1,n2,soma))
    if escolha == 2:
        multiplicar = n1 * n2
        print('Você multiplicou os valores {} e {} , obtendo {}.'.format(n1, n2, soma))
    if escolha == 3:
        if n1 > n2:
            print('{} é MAIOR que {}.'.format(n1,n2))
        elif n2 > n1:
            print('{} é MAIOR que {}.'.format(n2,n1))
        else:
            print('Os valores são IGUAIS!')
    if escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if escolha > 6:
        print('Escolha inválida! Tente novamente.')
    if escolha == 5:
        sleep(2),print('FINALIZADO...')
        print('Volte sempre.')
        break

#RESOLUÇÃO CURSO EM VÍDEO
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''\033[3;31m
    ------------------------------
    QUAL OPERAÇÃO DESEJA REALIZAR?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ------------------------------
    ''')
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('Você somou os valores {} e {} , obtendo {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('Você multiplicou os valores {} e {} , obtendo {}.'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print('{} é MAIOR que {}.'.format(n1,n2))
        elif n2 > n1:
            print('{} é MAIOR que {}.'.format(n2,n1))
        else:
            print('Os valores são IGUAIS!')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        sleep(2),print('Finalizado.')
        break

    else:
        print('Opção inválida! Tente novamente.')


