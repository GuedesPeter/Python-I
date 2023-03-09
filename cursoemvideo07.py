
#*OPERADORES ARITMÉTICOS*
'''
PARA TESTAR SE UMA COISA É IGUAL A OUTRA NO PYTHON,USAMOS O SINAL == (É IGUAL[==])
exemplo:
5 + 2 == 7     5 / 2 ==    5//2 ==
5 - 2 == 3     5 ** 2 ==
5 * 2 == 10    5 % 2 ==

ORDEM DE PRECEDENCIA:
1° ()--> Irá executar primeiro o que estiver dentro dos parênteses;
2° ** --> A EXPONÊNCIAÇÃO é a segunda na ordem de precedencia;
3° * / // % --> Terceiros na ordem de precedencia, e será executado o que aparecer primeiro;
4° + - --> SOMA E SUBTRAÇÃO binária são as quartas na ordem de precedencia.

#EXEMPLO 1:
# 4°  3° ordem precedencia
5 + 3 * 2 == 11
# 3°  4°  2° ordem precedencia
3 * 5 + 4 ** 2 == 31
# 3°   1°   2° ordem precedencia
3 * (5 + 4) ** 2 == 243
'''
'''nome= input('Qual é seu nome?')
print('Prazer em te conhecer {:=^10} !'.format(nome))
IMPRIME O .FORMAT COM FORMATAÇÕES
Exemplo do print da variavel(nome) acima:
==========(nome)==========
'''
''''#Usado APENAS para mostrar a soma na tela
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
'''
'''USAREMOS A SINTAXE COM AS {} AO INVÉS DE ","
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#\n QUEBRAS AS LINHAS
print('A soma é {} ,\n a multiplicação é {} ,\n a divisão é {:.3f}'.format(s,m,d))
print(' A div.inteira é {},\na exponenciação é {}'.format(di,e))'''

#DESAFIO 01:
'''Faça um programa que leia um numero inteiro na tela e seu
sucessor e antecessor'''
#RESPOSTA:
'''
n = int(input('Digite um número: '))
print('O seu antecessor é {} e seu sucessor é {} !!'.format(n-1,n+1))
'''

#DESAFIO 02:
'''Crie um algoritmo que leia um número e mostre o seu dobro,triplo 
e raiz quadrada( raiz quadrada é só EXPONENCIAR o número por meio 1/2
e raiz cúbica EXPONENCIAR por 1/3)'''
#RESPOSTA:
'''
n = int(input('Digite um número: '))
print('Seu DOBRO é {}, seu TRIPLO é {} \ne sua RAIZ QUADRADA é {} !'.format(n*2,n*3,n**(1/2)))
'''

#DESAFIO 03:
'''Desenvolva um programa que leia as duas notas de um aluno, e
calcule e motre a sua média.
'''
#RESPOSTA:
'''
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
print('A soma das notas é {} !\n A média das notas é {}'.format(n1+n2,(n1+n2)/2))
'''

#DESAFIO 04:
'''Escreva um programa que leia um valor em metros,e o exiba
convertido em centímetros'''
#RESPOSTA:
'''
m = float(input('Digite o valor em metros: '))
print('O seu valor em centímetros é de {}'.format(m*100))
'''

#DESAFIO 05:
'''Faça um programa que leia um número inteira qualquer
e mostre na tela sua tabuada'''
#RESPOSTA:
'''
n = int(input('Digite um número: '))
print('*0={}\n*1={}\n*2={}\n*3={}\n*4={}\n*5={}\n*6={}\n*7={}\n*8={}\n*9={}\n*10={}'.format(n*0,n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10))'''

#DESAFIO 06:
'''Crie um programa que leia quanto uma pessoa tem na carteira,
e mostre quantos dolares ela pode comprar.
Considere US$1.00 = R$3,27'''
#RESPOSTA:
'''
s = float(input('Digite o seu saldo(R$): '))
print('Você pode comprar {:.2f} Dólares!'.format(s/3.27))
'''

#DESAFIO 07:
'''Faça um programa que leia a largura e a altura de uma parede em
metros,calcule a sua área e a quantidade de tinta para pinta-la,
sabendo que cada litro de tinta pinta uma área de 2m**2'''
#RESPOSTA:
'''
l = float(input('largura (m): '))
a = float(input('altura (m): '))
print('Sua área mede {}\n e é necessário para pinta-la {} litros de tinta'.format(l*a,(l*a)/0.2))
'''

#DESAFIO 08:
'''Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço,com 5% de desconto'''
#RESPOSTA:
'''
p = float(input('Digite o valor do produto: '))
d = (p * 0.05)
print('O produto custa {} R$\n E seu valor com 5% de desconto é de {}!'.format(p,p-d))
'''

#DESAFIO 09:
'''Ffaça o algoritmo que leia o salario de um funcionário e 
mostre seu novo salário com 15% de aumento'''
#RESPOSTA
'''
s = float(input('Digite o seu salário(R$): '))
a = (s * 0.15)
print('Você ganhava R${:.2f} \nE obteve um aumento de 15% no seu salário,passando a ganhar R${:.2f} .'.format(s,s+a))
'''