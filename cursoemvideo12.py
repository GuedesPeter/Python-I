'''
2° MUNDO PYTHON - ESTRUTURAS DE CONTROLE:

CONDIÇÕES ANINHADAS
IF - ELIF - ELSE

Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
usando os comandos if.. elif.. else em programas Python.




'''

#EX.:
nome = input('Qual é seu nome? ')
if nome =='Paulo':
    print('Que nome lindo...')
elif nome == 'Maria'or nome == 'João':
    print('Seu nome é bem popular...')
elif nome in 'Ana , Claudia , Jéssica , Juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é normal...')
print('Tenha um bom dia!')
