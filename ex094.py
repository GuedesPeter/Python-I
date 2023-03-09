

'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média

'''
lista = []
pessoa = dict()
soma = media = 0
#CÓDIGO PARA DAR ENTRADA NOS DADOS
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor,digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        continuar = input('Deseja continuar [S/N]?').upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite somente S ou N.')
    if continuar == 'N':
        break
print(lista)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'A média de idade das pessoas é de {media:5.2f}')
print('As mulheres cadastradas foram:',end='')
for p in lista:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ',end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v} ',end='')
        print()
print('>>>ENCERRADO<<<')




