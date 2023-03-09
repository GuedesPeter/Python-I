


'''
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
'''


n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

if n1 > n2 :
    print('O \033[2;36;42mPRIMEIRO valor é maior!!')
elif n2 > n1:
    print('O \033[3;33;44mSEGUNDO valor é maior!!')
else:
    print('\033[4;35;41mNão existe valor maior, os dois são iguais!')
