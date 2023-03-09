

'''
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.

'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Por favor, digite um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! Por favor, digite um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n



#PROGRAMA PRINCIPAL



inteiro = leiaInt('Digite um valor inteiro: ')
print(f'\033[32mO valor digitado foi {inteiro}.\033[m')

real = leiaFloat('Digite um valor real: ')
print(f'\033[35mO valor real digitado foi {real}.\033[m')
