


'''Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''

n = str(input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print('Muito prazer te conhecer!')
print('Seu primeiro nome é : {}'.format(nome[0]))
print('Seu ultimo nome é : {}'.format(nome[len(nome)-1]))

'''Usando o len() para saber quantas posições tem Nome
e mostrar o len() de Nome na posição
- 1 para não retornar a posição zero'''



