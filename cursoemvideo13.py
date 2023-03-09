

'''
ESTRUTURAS DE REPETIÇÃO:   FOR

- LAÇO COM VARIÁVEL DE CONTROLE
-----------------------------
LAÇO C NO INTERVALO(1,10):
    PASSO
PEGA
-----------------------------
FOR C IN RANGE(1,10):
    PASSO
PEGA
-----------------------------

LAÇO C NO INTERVALO(0,3):
    SE MOEDA:
        PEGA
    PASSO
    PULA
PASSO
PEGA

------------------------------
FOR C IN RANGE(0,3):
    IF MOEDA:
        PEGA
    PASSO
    PULA
PASSO
PEGA
-------------------------------
OBS: O ULTIMO NÚMERO NÃO É CONSIDERADO
'''


#EX1.:

print('EX1.:')
for oi in range(1,7):
    print(oi)
print('FIM.')
print('--'*30)

#REALIZANDO A CONTAGEM AO CONTRÁRIO
print('REALIZANDO A CONTAGEM AO CONTRÁRIO')
for oi in range(7,0,-1):
    print(oi)
print('FIM.')
print('--'*30)

#REALIZANDO CONTAGEM PULANDO NÚMEROS
#ZERO A 7 PULANDO DE 2 EM 2 (NESTE CASO)
print('''REALIZANDO CONTAGEM PULANDO NÚMEROS
ZERO A 7 PULANDO DE 2 EM 2 (NESTE CASO)''')
for oi in range(0,7,2):
    print(oi)
print('FIM.')
print('--'*30)

print('--'*30)
n = int(input('Digite um número: '))

#REALIZANDO UM CONTADOR
print('REALIZANDO UM CONTADOR')
for contador in range(0,n+1):
    print(contador)
print('FIM')
print('--'*30)

#REALIZANDO CONTADOR PASSO A PASSO
print('REALIZANDO CONTADOR PASSO A PASSO')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))

for contador in range(inicio,fim+1,passo):
    print(contador)
print('FIM!')

print('--'*30)

#VARIÁVEL PARA INSERIR DADOS DENTRO DO LAÇO
print('VARIÁVEL PARA INSERIR DADOS DENTRO DO LAÇO')

for contador in range(0,5):
    nome = input('Digite o nome:')
print('FIM')
print('--'*30)

#REALIZANDO SOMATÓRIO DOS VALORES DA VARIÁVEL DENTRO DO FOR
print('REALIZANDO SOMATÓRIO DOS VALORES DA VARIÁVEL DENTRO DO FOR: ')

soma = 0
for contador in range(0,5):
    valor = int(input('Digite um valor: '))
    soma += valor
print('O somatório de todos os valores foi {}.'.format(soma))
print('FIM')

