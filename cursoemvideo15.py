

'''
Nessa aula, vamos aprender como utilizar a instrução break e os
loopings infinitos a favor das nossas estratégias de código.
É muito importante saber usar o break no Python,
á que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso,
vamos aprender como trabalhar com as novas fstrings do Python.

>> while true <<

'''

n = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
print(f'A soma é {soma}.')

