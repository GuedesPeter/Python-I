

'''Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo.'''

'''
REGRA MATEMÁTICA:
Cada segmento tem que ser MENOR
que a soma dos segmentos dos outros dois'''

print('=='*20)
print(('ANALISANDO TRIÂNGULOS: '))
reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))


if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Este segmento pode formar um Triângulo.')
else:
    print('Este Segmento NÃO pode formar um Triângulo!')



