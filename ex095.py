

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.

'''
#-------------INICIO DO PROGRAMA : ENTRADA DE DADOS DOS JOGADORES---------------------
time = []
partidas = []
jogador = dict()
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    total = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,total):
        partidas.append(int(input(f'Qauntos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    while True:
        continuar = input('Quer continuar [S/N]? ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if continuar =='N':
            break

print('--'*30)
#----------------------------------------------------------------------------------

#----------------------------ANÁLISE DOS DADOS-------------------------------------
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('--'*30)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('--'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 FINALIZAR]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- ESTATÍSTICAS DO JOGADOR {time[busca]["nome"]}: ')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} Gols.')
        print('--'*30)
print('>>VOLTE SEMPRE<<')
#-------------------------------------------------------------------------------------
