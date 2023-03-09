'''
Nessa aula, vamos aprender o que são TUPLAS
e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis
que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.

VARIÁVEIS COMPOSTAS - TUPLAS

TUPLAS SÃO DECLARADAS ENTRE PARÊNTESES ()
- AS TUPLAS SÃO IMUTÁVEIS,OU SEJA,NÃO POSSO ALTERAR SEU CONTEÚDO.
NÃO POSSO MUDAR UMA TUPLA.


'''
'''
lanche = ("Hamburguer","Suco","Pizza","Pudim")
print(lanche[0])
print((lanche[:2]))
print(lanche[1:])
print(lanche[-1])#RETORNA O ULTIMO ELEMENTO POIS O (-) RETORNA AS POSIÇÕES AO CONTRÁRIO
print(len(lanche))#RETORNA O TAMANHO DA TUPLA(NÚMERO DE ELEMENTOS) - LEN()
#PARA REPETIÇÃO ELE IMPRIME UM ELEMENTO O ARMAZENANDO NA VARIÁVEL DE CONTROLE(C)
for c in lanche:
    print(c)
'''
#---------------------------------------------------------------------#

lanche = ("Hamburguer","Suco","Pizza","Pudim","Batata Frita")
for comida in lanche:
    print(f'Eu vou comer: {comida}!')
print('--'*30)

for contador in range(0,len(lanche)):
    print(f'Eu vou comer: {lanche[contador]} na posição {contador}')
print('--'*30)
#   INDICE ,ELEMENTO
for posicao,comida in enumerate(lanche):
    print(f'Eu vou comer: {comida} na posição {posicao}')
print('--'*30)
#MANDA MOSTRAR O 'LANCHE' EM ORDEM - METODO SORTED(),ORDENADO.
print(sorted(lanche))

print('--'*30)
#UNINDO AS TUPLAS - ATRAVES DA SOMA DELAS ATRIBUIDA A VARIÁVEL 'C'
#OBS: A ORDEM DAS TUPLAS TEM INTERFERENCIA A+B NÃO É IGUA A B+A
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print('--'*30)
#RETORNA A QTDE. DE ELEMENTOS DA TUPLA
print(len(c))
#RETORNA A QTDE DE VEZES QUE O ELEMENTO ESTIPULADO APARECE DENTRO DA TUPLA
print(c.count(5))

print('--'*30)
#RETORNA O ÍNDICE DO ELEMENTO ESCOLHIDO DENTRO DA TUPLA
print(c.index(8))
print('--'*30)

#POSSO TER DADOS DE TIPOS DIFERENTES DENTRO DA TUPLA
pessoa = ("Gustavo",39,'M',99.88)
#POSSO APAGAR TODA A VARIÁVEL - TUPLA
# del(pessoa)
print(pessoa)
