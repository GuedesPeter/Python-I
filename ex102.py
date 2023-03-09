

'''
Crie um programa que tenha uma função fatorial()
que receba dois parâmetros:
o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo
do fatorial.

'''

def fatorial(n,show=False):
    """
    >> CALCULA O FATORIAL DE UM NÚMERO
    :param n: Número a ter seu fatorial calculado
    :param show: Se True mostra o calculo, se False não mostra
    :return: Resultado do fatorial
    """
    fator = 1
    for cont in range(n,0,-1):
        if show:
            print(cont,end='')
            if cont > 1:
                print(f' x ',end='')
            else:
                print(' = ',end='')
        fator *= cont
    return fator


'''PROGRAMA PRINCIPAL'''
print(fatorial(5,True))
print('-'*50)
help(fatorial)
