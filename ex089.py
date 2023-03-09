

'''
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo
a média de cada um e permita que o
usuário possa mostrar as notas de cada aluno individualmente.

'''

cadastro = []
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Digite a 1° Nota: '))
    nota2 = float(input('Digite a 2° Nota: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome,[nota1,nota2],media])

    continuar = input('Deseja continuar [S/N] ? ')
    if continuar in 'Nn':
        break
print('--'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('--'*30)
for i , a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('--'*30)
    opcao = int(input('Escolha o número do aluno para ver suas notas [999 PARA FINALIZAR]: '))
    if opcao == 999:
        print('FINALIZADO')
        break
    if opcao <= len(cadastro)- 1:
        print(f'Notas de {cadastro[opcao][0]} são : {cadastro[opcao][1]}')
        