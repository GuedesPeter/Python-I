

'''

ESTRUTURAS DE REPETIÇÃO:  WHILE

** ESTRUTURA DE REPETIÇÃO COM TESTE LÓGIOCO **

GERALMENTE O WHILE É USADO QUANDO EU NÃO SEI O NÚMERO DE
REPETIÇÕES PARA EXECUTAR O LAÇO

COM O WHILE AO INVÉS DE COLOCAR UM INTERVALO (TIPO O RANGE NO FOR)
EU COLOCO UMA CONDIÇÃO - TRUE


EX.:
>> WHILE NOT <<
'ENQUANTO NÃO' CHEGAR NA MAÇÃ
    PASSO
PEGA
------------------------------
WHILE NOT MAÇA:
    PASSO
PEGA

------------------------------

EX.:

>> WHILE NOT <<
'ENQUANTO NÃO' CHEGAR NA MAÇÃ:
    SE TIVER CHÃO:
        PASSO
    SE TIVER BURACO:
        PULA
    SE TIVER MOEDA:
        PEGA
PEGA
--------------------------------
WHILE NOT MAÇÃ:
    IF TIVER CHÃO:
        PASSO
    IF TIVER BURACO:
        PULA
    IF TIVER MOEDA:
        PEGA
PEGA

'''

#PRÁTICA:
'''
for contador in range(1,10):
    print(contador)
print('FIM')
'''
'''
contador = 1

while contador < 10:
    print(contador)
    contador +=1
print('FIM')

'''
'''
for contador in range(1,5):
    num = int(input('Digite um valor: '))
print('FIM')
'''
'''
n = 1
# enquanto o num for diferente de zero ele continua executando o laço
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
'''
'''
#Enquanto a RESPOSTA for igual a 'S' ele continua executando o laço
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = input('Quer continuar? [S/N]:').upper()
print('FIM')
'''

num = 1
par = 0
impar = 0
while num != 0:
    num = int(input('Digite um valor: '))
    #Teste funciona somente se o num for diferente de zero
    if num != 0:
        if num % 2 == 0:
            par +=1
        else:
            impar +=1
print('Você digitou {} números PARES  e {} números ÍMPARES.'.format(par,impar))
print('Acabou!!!')

