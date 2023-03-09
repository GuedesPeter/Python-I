

'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.

'''

from random import randint


contador = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = input("PAR ou ÌMPAR? [P/I] : ").strip().upper()[0]
    print(f'O Computador jogou {computador} - Você jogou {jogador}. Total {total}.')
    if escolha == 'P':
        if total % 2 == 0:
            print('GANHOU!')
            contador += 1
        else:
            print('PERDEU!')
            break

    if escolha == 'I':
        if total % 2 == 1:
            print('GANHOU!')
            contador += 1
        else:
            print('PERDEU!')
            break
print(f'FIM DE JOGO! VOCÊ VENCEU {contador} VEZES!')
