

'''
VARIÁVEIS COMPOSTAS - DICIONÁRIOS

Os dicionários são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.


DICIONÁRIOS EM PYTHON SÃO IDENTIFICADOS POR CHAVES {}

DADOS = {'NOME':'PEDRO'.'IDADE':'25'}
PRINT(DADOS['NOME']) --- 'PEDRO'
PRINT(DADOS['IDADE') --- '25'

PARA ADICIONAR ELEMENTOS AO DICIONÁRIO O METODO .APPEND() NÃO FUNCIONA
ADICIONAMOS ELEMENTOS DESTA FORMA:

DADOS['SEXO'] = 'M'
DADOS = {'NOME':'PEDRO'.'IDADE':'25','SEXO':'M'}

PARA REMOVER ELEMENTOS USAMOS O DEL
DEL DADOS['IDADE']


FILME = {
    'TITULO':'STAR WARS',
    'ANO':'1977',
    'DIRETOR':'GEORGE LUCAS'
}

PRINT(FILME.VALUES()) - RETORNA TODOS OS VALORES DO MEU DICIONÁRIO
PRINT(FILME.KEYS())  - RETORNA TODAS AS CHAVES DO MEU DICIONÁRIO
PRINT(FILME.ITEMS()) - RETORNARÁ OS VALORES E AS CHAVES

EX:

FOR K,V IN FILME.ITEMS():
    PRINT(F'O {K} É {V}'
    'O TÍTULO É STAR WARS'
    'O ANO É 1977'
    'O DIRETOR É GEORGE LUCAS'


POSSO CRIAR UMA ESTRUTURA ONDE JUNTO TUPLAS,LISTAS E DICIONÁRIOS

POSSO CRIAR UMA LISTA ONDE CADA ELEMENTO TEM UM DICIONÁRIO DENTRO
EX:
LOCADORA = [{'TITULO':'STAR WARS','ANO':'1977','DIRETOR':'GEORGE LUCAS'}
            {'TITULO':'AVANGERS','ANO':'2012','DIRETOR':'JOSS WHEDON'}
            {'TITULO':'MATRIX','ANO':'1999','DIRETOR':'WACHOWSKI'}
]
OBS: OBSERVE QUE AS LISTAS SÃO IDENTIFICADAS POR NÚMEROS[0] E OS
DICIONÁRIOS POR TEXTOS{'TITULO'}

PRINT(LOCADORA[0]['ANO']) -----> '1977'
PRINT(LOCADORA[2]['TITULO'] -------> 'MATRIX'


O DICIONÁRIO NÃO TEM 'ENUMERATE',EU DEVO USAR O ITEMS()

for k,v in pessoas.items():
    print(f'{k} = {v}')


'''

pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('--'*30)
print(pessoas.keys())
print('--'*30)
print(pessoas.values())
print('--'*30)
print(pessoas.items())
print('--'*30)
for k in pessoas.keys():
    print(k)

print('--'*30)
for k in pessoas.values():
    print(k)
print('--'*30)
for k in pessoas.items():
    print(k)
print('--'*30)

#O DICIONÁRIO NÃO TEM 'ENUMERATE',EU DEVO USAR O ITEMS()
for k,v in pessoas.items():#ITEMS() AO INVÉS DE ENUMERATE
    print(f'{k} = {v}')

print('--'*30)

brasil = [] #LISTA
estado1 = {'uf':'Rio Grande do Sul','sigla':'RS'} #DICIONÁRIO
estado2 = {'uf':'Rio de Janeiro ','sigla':'RJ'} #DICIONÁRIO
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0])
print('--'*30)
print(brasil[0]['uf'])
print('--'*30)
print(brasil[0]['sigla'])
print('--'*30)

estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())
    # USAR O METODO COPY() NO DICIONÁRIO PARA GERAR UMA CÓPIA
    # EVITANDO A RELAÇÃO DENTRO DA LISTA(REPETIÇÃO)
print(brasil)

print('--'*30)

for e in brasil:
    print(e)

print('--'*30)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

print('--'*30)

for e in brasil:
    for v in e.values():
        print(v,end='  ')
    print()



