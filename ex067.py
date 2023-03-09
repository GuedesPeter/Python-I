

'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo

'''



while True:
    num = int(input('TABUADA DO : '))
    print('--' * 10)
    if num < 0 :
        break

    for contador in range(1,11):
        print(f'{num} x {contador} = {num*contador}')
    print('--'*10)
print('FINALIZADO')
