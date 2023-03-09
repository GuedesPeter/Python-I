

'''
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.

'''

aluno = {
    'NOME':input('NOME DO ALUNO: '),
    'MEDIA':float(input('MÉDIA DO ALUNO: '))


}
if aluno['MEDIA'] >= 7:
    aluno['SITUAÇÃO'] = 'APROVADO'
elif 5 <= aluno['MEDIA'] < 7:
    aluno['SITUAÇÃO'] = 'EM RECUPERAÇÃO'
else:
    aluno['SITUAÇÃO'] = 'REPROVADO'

print('--'*30)
for k,v in aluno.items():
    print(f'{k} : {v}')

'''
print('--'*30)
print(f'Nome do aluno: {aluno["NOME"]}')
print(f'Média do aluno: {aluno["MEDIA"]}')
print(f'Situação: {aluno["SITUAÇÃO"]}')
'''