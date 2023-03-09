'''Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais
ele foi alugado.Calcule o preço a pagar,sabendo que o carro
custa R$60,00 por dia e R$0,15 por km rodado.'''

distancia = float(input('Digite a quantidade de KM percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (dias * 60) + (distancia * 0.15)
print('O valor final a pagar,somando diárias e km rodados,é de R${:.2f}.'.format(valor))
