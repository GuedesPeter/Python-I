

'''
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.

'''
#MINHA SOLUÇÃO:
def area():
    print('-'*18)
    print('CALCULANDO TERRENO')
    print('-' * 18)
    l = float(input('Largura: '))
    c = float(input('Comprimento: '))
    terreno = l * c
    print(f'A área do terreno {l} x {c} mede {terreno}m².')


#----PROGRAMA PRINCIPAL----
area()

#SOLUÇÃO CURSO EM VIDEO:

def área(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} mede {a}m²')


#----PROGRAMA PRINCIPAL----
print('-'*18)
print('CALCULANDO TERRENO')
print('-' * 18)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
área(l,c)
