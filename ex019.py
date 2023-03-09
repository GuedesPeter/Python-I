'''Um professor quer sortear um dos seus quatro alunos
para apagar o quadro.Faça um programa que ajude ele,lendo
o nome dos alunos e escrevendo na tela o nome
de escolhido.'''



from random import choice
a1 = input('Aluno 1 : ')
a2 = input('Aluno 2 : ')
a3 = input('Aluno 3 : ')
a4 = input('Aluno 4 : ')
#CRIAR UMA LISTA
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
'''CHOICE ESCOLHE UM ALUNO DE FORMA ALEATÓRIA'''