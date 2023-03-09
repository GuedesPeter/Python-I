'''Faça um programa que leia a AULTURA  ea LARGURA de uma
parede em metros,calcule sua área e a quantidade de tinta
necessária para pinta-la,sabendo que cada litro de tinta
pinta uma área de 2 metros'''

larg = float(input('Digite a largura : m²'))
altura = float(input('Digite a altura : m²'))
area = larg * altura
tinta = area / 2
print('A parede tem dimenssão de {} x {} m², sua área é de {} m².\n Serão necessários {:.1f}L de tinta para pinta-la.'.format(larg,altura,area,tinta))
