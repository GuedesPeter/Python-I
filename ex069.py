

'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se
usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.

'''

total18 = 0
totalH = 0
totalM = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if total18 >= 18:
        total18 += 1
    if sexo == 'H':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM += 1
    resposta = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if resposta == 'N':
        print('FINALIZADO.')
        break
print(f'A) {total18} Pessoas tem mais de 18 anos.')
print(f'B) {totalH} Homens foram cadastrados.')
print(f'C) {totalM} Mulheres tem menos de 20 anos.')


