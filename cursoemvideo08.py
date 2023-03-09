'''UTILIZANDO MÓDULOS'''
#IMPORTOU MATEMÁTICA(MATH),
'''ALGUMAS FUNÇÕES DO MODULO MATH:
CEIL - FAZ ARREDONDAMENTOS PARA CIMA
FLOOR - FAZ ARREDONDAMENTOS PARA BAIXO
TRUNC - ELIMINA O NÚMERO DA VIRGULA PARA FRENTE SEM FAZER ARREDONDAMENTOS
POW - (POWER)CALCULA POTÊNCIA **
SQRT - CALCULA A RAIZ QUADRADA
FACTORIAL - CALCULA O FATORIAL DE UM NÚMERO

IMPORT MATH - IMPORTA TODA A BIBLIOTECA
FROM MATH IMPORT SQRT - IMPORTA UM UNICO COMANDO,NESTE CASO A RAIZ QUADRADA
>>POSSO IMPORTAR MAIS DE UMA FUNCIONALIDADE COLOCANDO VIRGULA AO LADO DELAS
E INSERINDO A PROXIMA FUNCIONALIDADE DESEJADA.
EX.: FROM MATH IMPORT POW,CEIL,FLOOR'''


#EX1.:
'''TODAS AS FUNCIONALIDADES

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.'.format(num,math.ceil(raiz)))

'''

#EX2.:
'''IMPORTANDO UMA FUNCIONALIDADE ESTECÍFICA

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))
'''


#EX3.:

'''Importa da biblioteca RANDOM,onde o computador retorna números aleatórios
entre 0 e 1 ou RANDIT que retorna números inteiros

import random
num = random.randit(1,10)
print(num)

'''
#EX4.:
'''
#INSERINDO MÓDULOS(VIDE CADERNO)
import emoji
#USAR A FUNÇÃO EMOJIZE,COLOCAR VIRGULA E APÓS INSERIR USE_ALIASES=TRUE
print(emoji.emojize('Olá mundo :sunglasses:',use_aliases=True))
'''

#EXERCÍCIOS:

#1
'''Crie um programa que leia um número real qualquer pelo teclado e mostre sua porção
inteira EX.:
-Digite um número: 6.127
- O número 6.127 tem a parte inteira 6
#MINHA RESOLUÇÃO:
1°
from math import trunc
num = float(input('Digite um número: '))
por = trunc(num)
print('O número {} tem a parte inteira {}'.format(num,por))

2°
from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num,trunc(por)))

'''

'''Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo,calcule e mostre o comprimento da hipotenusa
#MINHA RESOLUÇÃO:
1°
import math
cop = float(input('Cateto Oposto: '))
cop1 = pow(cop,2)
cad = float(input('Cateto Adjacente: '))
cad1 = pow(cad,2)
h = (cop1 + cad1)
print('Cateto Oposto mede {} , Cateto Adjacente mede {}, Hipotenusa mede {}'.format(cop,cad,h))

2°
#import math 
from math import hypot
cop = float(input('Cateto Oposto: '))
cad = float(input('Cateto Adjacente: '))
h = math.hypot(cop,cad)
print('A Hipotenusa vai medir {:.2f}'.format(h))


'''

'''Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno,cosseno e tangente desse ângulo
#MINHA RESOLUÇÃO:

from math import sin,cos,tan
ang = float(input('Digite o ângulo: '))
seno = sin(ang)
cosseno = cos(ang)
tange = tan(ang)
print('O seno,cosseno e tangente de {} são: {:.2f}, {:.2f}, {:.2f}'.format(ang,seno,cosseno,tange))

2°
from math import sin,cos,tan
ang = float(input('Digite o ângulo: '))
#converter os radianos para centígrados
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tange = tan(radians(ang))

print('O seno,cosseno e tangente de {} são: {:.2f}, {:.2f}, {:.2f}'.format(ang,seno,cosseno,tange))




'''

'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = input('Aluno 1 : ')
a2 = input('Aluno 2 : ')
a3 = input('Aluno 3 : ')
a4 = input('Aluno 4 : ')
#CRIAR UMA LISTA
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''





'''O mesmo professor do desafio anterior quer sortear a o rdem de apresentação
de trabalhos dos alunos.Faça um programa que leia o nome doa quatro alunos e mostre a
ordem sorteada.


from random import shuffle
a1 = input('Aluno 1:')
a2 = input('Aluno 2:')
a3 = input('Aluno 3:')
a4 = input('Aluno 4:')
lista = [a1,a2,a3,a4]
#EMBARALHAR A LISTA
shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)'''

'''Faça um programa em Python 
que abra e reproduza um audio em MP3'''
