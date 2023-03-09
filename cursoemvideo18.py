

'''
VARIÁVEIS COMPOSTAS
LISTAS - PARTE 2

As listas são variáveis compostas que permitem armazenar vários valores
em uma mesma estrutura, acessíveis por chaves individuais.

CRIANDO CÓPIDA DA LISTA [:]

DADOS = ['PEDRO,25]
DADOS.APPEND('PEDRO')
DADOS.APPEND(25)

PESSOAS = []
PASSOAS.APPEND(DADOS[:])  <<<<<<<<<  GEREI UMA CÓPIA DE DADOS[:]
PESSOAS = ['PEDRO',25]
             0      1
          -------------
                0

EX:
INSERINDO ESTRUTURAS (LISTAS DENTRO DE LISTAS)
------------------------------------------------------------
PESSOAS = [ ['PEDRO,25] , ['MARIA',19] , ['JOÃO',32] ]
               0     1       0      1       0     1
           -------------  -------------  ---------------
                  0              1              2
------------------------------------------------------------


PRINT(PESSOAS[0][0]) >>> 'PEDRO'
PRINT(PESSOAS[1][1]) >>>    19
PRINT(PESSOAS[2][0]) >>>  'JOÃO'
PRINT(PESSOAS[1])    >>>  ['MARIA',19]


'''

'''
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) #FAÇO A CÓPIA DA LISTA
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #FAÇO A CÓPIA DA LISTA
print(galera)
'''
#------------------- LENDO NOME E IDADE ---------------------------
'''
galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
#print(galera[3][0])

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

'''
print('--'*30)


galera = []
dado = []
for c in range(0,3):
    dado.append(input('NOME: '))
    dado.append((int(input('IDADE: '))))
    galera.append(dado[:]) #COLOCO UMA CÓPIA PARA EVITAR REPETIÇÃO
    dado.clear() # APO´S A COPIA LIMPO A LISTA DADOS,CASO NÃO HOUVER
    #COPIA SERÁ LIMPO TODAS AS LISTAS
print(galera)

#---------------- ANALISANDO MAIOR E MENOR DE IDADE -------------------
total_maior = 0
total_menor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} pessoas maiores de idade e \n{total_menor} pessoas menores de idade')

