

'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt(‘Digite um n: ‘)

'''

def leiaInt(msg):
    i = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            i = True
        else:
            print('Você não digitou um número!')
        if i:
            break
    return valor



#PROGRAMA PRINCIPAL

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
