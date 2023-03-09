'''
VARIÁVEIS COMPOSTAS

LISTAS []- (PARTE 1)

Nessa aula, vamos aprender o que são LISTAS
e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores
em uma mesma estrutura, acessíveis por chaves individuais.


LANCHE = ['HAMBURGUER','SUCO','PIZZA','PUDIM']
-------------------------------------------------
AS LISTAS SÃO MUTÁVEIS:

LISTA[3] = 'PICOLÉ'
LANCHE = ['HAMBURGUER','SUCO','PIZZA','PICOLÉ']

PARA ADICIONAR ELEMENTOS NA LISTA USAMOS O MÉTODO(COMANDO)
.APPEND()
ESTE COMANDO ADICIONA O ELEMENTO NO FINAL DA LISTA
EX:
LISTA.APPEND('COOKIE')
LANCHE = ['HAMBURGUER','SUCO','PIZZA','PICOLÉ','COOKIE']
              0           1      2       3        4

PARA ADICIONAR UMA ELEMENTO EM UMA POSIÇÃO ESPECÍFICA
USAMOS O MÉTODO(COMANDO)
.INSERT()

EX:
LISTA.INSERT(0,'HOT-DOG')
LANCHE = ['HOT-DOG','HAMBURGUER','SUCO','PIZZA','PICOLÉ','COOKIE']
              0          1         2      3        4        5

PARA REMOVER UM ELEMENTO EM UMA POSIÇÃO ESPECÍFICA
USAMOS O MÉTODO(COMANDO)
.POP()
ELE GERALMENTE ELIMINA O ULTIMO ELEMENTO DA LISTA MAS POSSO ESCOLHER
E INSERIR UM ÍNDICE

LISTA.POP(3)

PODEMOS USAR TAMBÉM O MÉTODO(COMANDO) .REMOVE()
NESTE PASSAMOS O NOME DO ELEMENTO A SER REMOVIDO COMO PARÂMETRO

LISTA.REMOVE('PIZZA')

PODEMOS CRIAR UMA LISTA ATRAVÉS DE UM RANGE:
VALORES = LIST(RANGE(4,11))
VALORES [4,5,6,7,8,9,10]
ESTE MÉTODO CRIA OS ELEMENTOS EM ORDEM DEVIDO AO RANGE

VALORES = [8,2,5,6,4]
PARA ORDENAR OS VALORES DE UMA LISTA EU USO MÉTODO .SORT()
VALORES.SORT()
VALORES = [2,4,5,6,8]

ORDEM INVERSA USAMOS
VALORES.SORT(REVERSE=TRUE)

PARA SABERMOS O TAMANHO DA LISTA USAMOS O LEN()
E ELE RETORNA A QUANTIDADE DE ELEMENTOS DA LISTA
'''


num = [2,5,9,1]
num[3] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2,2)
#O .REMOVE() VARRE TODA A LISTA E CASO TENHA NÚMEROS IGUAIS
# ELE REMOVERÁ O PRIMEIRO QUE APARECER
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4 na lista para ser removido.')
print(num)
print(f'Esta lista tem {len(num)} elementos!')
print('--'*40)
#---------------------------------------------------------------------
valor = []
valor.append(5)
valor.append(9)
valor.append(4)

for v in valor:
    print(f'{v}...',end='')

print('--'*40)
#---------------------------------------------------------------------
for pos,v in enumerate(valor):
    print(f'Na posição {pos} encontrei o valor {v}.')

print('--'*40)
#---------------------------------------------------------------------
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
#---------------------------------------------------------------------
print('--'*40)

a = [2,3,4,7]
#fazendo b receber uma cópia dos valores evitando do PYTHON fazer uma ligação
b = a[:]
b[2] = 8
print(f'LISTA A: {a}')
print(f'LISTA B: {b}')
