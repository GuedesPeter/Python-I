'''
 Crie um programa que leia duas notas de um aluno e calcule sua média
 mostrando uma mensagem no final, de acordo com a média atingida:

 – Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

'''

nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Com notas {} e {},a sua média é {}. '.format(nota1,nota2,media))
    print('PARABÉNS! VOCÊ FOI APROVADO.')
elif media < 5:
    print('Com notas {} e {},a sua média é {}. '.format(nota1, nota2, media))
    print('REPROVADO!')
else:
    print('Com notas {} e {},a sua média é {}. '.format(nota1, nota2, media))
    print('VOCÊ FICOU EM RECUPARAÇÃO! ESTUDE MAIS.')
