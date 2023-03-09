


'''
Desenvolva um programa que leia
o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

'''

print('\033[0;30m=='*20)
print('\033[4;31m10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('\033[0;30m=='*20)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for pa in range(primeiro,decimo + razao,razao):
    print('{} '.format(pa),end=' >> ')
print(' FIM!')


