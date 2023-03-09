'''

 Refaça o DESAFIO 35 dos triângulos,
 acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes



'''


reta1 = float(input('Primeiro Segmento: '))
reta2 = float(input('Segundo Segmento: '))
reta3 = float(input('Terceiro Segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Este segmento pode formar um Triângulo ',end= '')
    if reta1 == reta2 and reta2 == reta3:
        print('EQUILÁTERO.')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')

else:
    print('Os segmentos acima não formam um triângulo!')

