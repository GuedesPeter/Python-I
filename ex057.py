

'''
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado,
peça a digitação novamente até ter um valor correto.

'''
'''
#MINHA RESOLUÇÃO
sexo = 'MF'

while sexo in 'MF' :
    print('Digite SAIR para finalizar.')
    sexo = input('Digite seu sexo [M/F] : ').upper()[0].strip()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido! Digite novamente.')
    if sexo == 'SAIR'.upper():
        print('FIM!')

'''
#SOLUÇÃO DO CURSO EM VÍDEO:

sexo = str(input('Digite seu sexo [M/F] : '))
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso!'.format(sexo))
    