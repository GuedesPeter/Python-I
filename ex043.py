

'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''

peso = float(input('Digite seu peso: KG '))
altura = float(input('Digite sua altura: m'))
imc = peso / (altura**2)

if imc < 18.5:
    print('Você pesa {}Kg e mede {}m - Seu IMC {:.2f} - Voce está ABAIXO DO PESO.'.format(peso,altura,imc))
elif imc >= 18 and imc <= 24:
    print('Você pesa {}Kg e mede {}m - Seu IMC {:.2f} - Voce está com PESO NORMAL.'.format(peso,altura,imc))
elif imc >= 25 and imc <= 29:
    print('Você pesa {}Kg e mede {}m - Seu IMC {:.2f} - Voce está com SOBREPESO.'.format(peso,altura,imc))
elif imc >= 30 and imc <= 40:
    print('Você pesa {}Kg e mede {}m - Seu IMC {:.2f} - Voce está OBESO.CUIDADO!.'.format(peso, altura, imc))
else:
    print('Você pesa {}Kg e mede {}m - Seu IMC {:.2f} - Voce está com OBESIDADE MÓRBIDA.DANGER!!!.'.format(peso, altura, imc))
