

'''

FUNÇÕES (PARTE 1)

Funções são trechos de código
que podem ser executados em momentos diferentes de nossos códigos.
Veja como funciona o comando def em Python
e como utilizá-lo com parâmetros simples e múltiplos.

TODAS AS FUNÇÕES EM PYTHON SÃO IDENTIFICADAS POR ()
NO FINAL DO NOME.
EX: PRINT() - INT() - FLOAT() - INPUT()





'''
'''
#EX1:

def mostralinha():
    print('--'*30)


#-------------------- PROGRAMA PRINCIPAL ----------------------------

mostralinha()
print('         SISTEMA DE ALUNOS        ')
mostralinha()
mostralinha()
print('         CADASTRO DE FUNCIONÁRIOS        ')
mostralinha()
mostralinha()
print('         ERRO DE SISTEMA        ')
mostralinha()

#EX2:
#FUNÇÃO COM PARÂMETROS
def mensagem(msg):
    print('--'*30)
    print(msg)
    print('--'*30)

#-------------------- PROGRAMA PRINCIPAL ----------------------------

mensagem('SISTEMA DE ALUNOS')


#EX3:

def titulo(txt):
    print('--'*30)
    print(txt)
    print('--'*30)

#-------------------- PROGRAMA PRINCIPAL ----------------------------

titulo('CURSO EM VÍDEO')
titulo('PYTON')

'''

#PRÁTICAS
'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

soma(4,5)
soma(8,9)
soma(2,1)
'''
#A FUNÇÃO SOMA RECEBE 2 PARÂMETROS
def soma(a,b):
    s = a + b
    print(f'A soma de {a} + {b} é igual a {s}.')

#-------- PROGRAMA PRINCIPAL --------------
soma(5,4)
soma(8,9)
soma(2,1)
#-------------------------------------------------------------------


def somar(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


#-------- PROGRAMA PRINCIPAL --------------
somar(2,4,6,8)



#-------------------------------------------------------------
'''O sinal de * dentro do parâmetro significa DESEMPACOTAR,ou seja
pode ser passado vários parâmetros dentro da função'''
def contador(*num):
        total = len(num)
        print(f'Recebi os valores {num},e são ao todo {total} números.')

#-----PROGRAMA PRINCIPAL ----
contador(1,2,3,4,5)

#-----------------------------------------------------------
def contagem(*num):
    for valor in num:
        print(f'{valor}',end=' ')
    print('FIM')

#-----PROGRAMA PRINCIPAL ----
contagem(1,2,3,4,5)

#----------------------------------------------------------
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*= 2
        pos +=1

#-----PROGRAMA PRINCIPAL ----
valores = [1,2,3,4,5]
dobra(valores)
print(valores)

#-----------------------------------------------------------

