

'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros

'''

valor = float(input('\033[7;35mValor do produto: R$ '))
opcao1 = valor - (valor*10/100)
opcao2 = valor - (valor*5/100)
opcao3 = valor
opcao4 = (valor + (valor*20/100))

print('\033[7;35m--'*30)

print('''\033[7;35mEscolha a forma de pagamento :

[1] - R${:.2f} á vista em dinheiro/cheque;
[2] - R${:.2f} á vista no cartão;
[3] - R${:.2f} em até 2X no cartão: preço formal;
[4] - R${:.2f} em 3X ou mais no cartão : 20% de juros.
'''.format(opcao1,opcao2,opcao3,opcao4))
print('\033[7;35m--'*30)
escolha = int(input('Digite sua escolha: '))


if escolha == 1:
    print('Você escolheu pagar o valor de R${:.2f} em dinheiro/cheque.'.format(opcao1))

elif escolha == 2:
    print('Você escolheu pagar R${:.2f} á vista no cartão.'.format(opcao2))

elif escolha == 3:
    print('Você escolheu pagar R${:.2f} em até 2x no cartão.'.format(opcao3))

elif escolha == 4:
    print('Você escolheu pagar R${:.2f} em 3x ou mais no cartão.'.format(opcao4))
    print('Esta opção possui acréscimo de 20% de juros. ')
    parcela = int(input('Em quantas vezes quer parcelar? '))
    total = opcao4 / parcela
    print('''O valor de sua compra R${:.2f} foi parcelado em {}X de R${:.2f} ao mês c/juros.'''.format(valor,parcela,total))

else:
    print('OPÇÃO INVÁLIDA.POR FAVOR ESCOLHA NOVAMENTE')




