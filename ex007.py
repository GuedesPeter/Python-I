'''Desenvolva um programa que leia duas notas de um aluno,
calcule e mostre a média'''

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
media = (nota1 + nota2)/2
print('O aluno {} tirou na primeira nota {},\n na segunda nota {},\n e ficou com média de {}.'.format(nome,nota1,nota2,media))
