

'''
FUNÇÕES (PARTE 2)

Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais
dinamismo em funções Python, escopo de variáveis e retorno de resultados.

>> INTERACTIVE HELP (AJUDA INTERATIVA) <<

HELP() - Temos acesso através deste comomando no console,as
informações tecnicas a respeito da linguagem.
Acessamos via ajuda interativa a documentação do PYTHON.
Para finalizar o comando help() no consele é só digitar QUIT.

Podemos tbm imprimir a documentação interna de cada funcionalidade.
Com isso podemos saber os parametros da funcionalidade escolhida.
EX:
print(input.__doc__)

-----------------------------------------------------------------------

>> DOCSTRINGS <<
É uma string de documentação(manual)
Quando coloco help(input),por exemplo,ele me retorna o manual da
função input()
Para criar uma DOCSTRIGS é só abrir aspas dupas 3 x logo abaixo
do comando DEF,assim posso criar o manual completo da minha função.
Exemplo:

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno

    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')

------------------------------------------------------------------------

>> PARÂMETROS OPCIONAIS <<
Adicionamos parametros nas funções com valores pré-definidos
fazendo com que eles se tornem opcionais e assim evitando erros.
Exemplo:

def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')


Ao chamar a função posso passar os 3 parametros,2 ,1 ou até mesmo
nenhum parâmetro.

somar(3,2,5)
somar(8,4)
somar(5)
somar()

-----------------------------------------------------------------------

>> ESCOPO DE VARIÁVEIS <<

Local onde a variável vai existir e onde ele vai deixar de existir
- Global : Pode ser definida fora da função(no programa principal)
e funcionar dentro da função,ou seja ela engloba tudo;

- Local : È declarada e funciona somente dentro da função

-------------------------------------------------------------------------

>> RETORNO DE VALORES <<
        RETURN

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s



resposta = somar(3,2,5)    ou   print(somar(3,2,5))   ou

r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(5,1)
print(f'Meus calculos deram {r1},{r2},{r3})

'''
#help(input)
#print(input.__doc__)

#---------------------------------------------------------------------

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno

    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM!')

contador(0,20,2)
print('-'*30)
help(contador)

#----------------------------------------------------------------------

def somar(a=0,b=0,c=0):
    """
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :observação: Os parâmetros são opcionais,pois já são
    pré-definidos
    """
    s = a+b+c
    print(f'A soma vale {s}')


#PROGRAMA PRINCIPAL

somar(3,2,5)
somar(8,4)
somar(5)
somar()
help(somar)

#------------------------------------------------------------------------
def teste():
    x = 8
    print(f'No programa principal n recebe {n}')
    print(f'No programa principal n recebe {n}')




#PROGRAMA PRINCIPAL
n = 2
print(f'No programa principal n recebe {n}')
teste()
'''
No caso abaixo dará ERRO,o X é uma variável local
e não poderei imprimi-la pois ela existe somente dentro da função 
teste() e não foi declarada fora da função.
TEM ESCOPO LOCAL
print(f'No programa principal x recebe {x}')
'''

#--------------------------------------------------------------------------------

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


#PROGRAMA PRINCIPAL --------------------------
r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(5,1)
print(f'Meus calculos deram {r1},{r2},{r3}')


#--------------------------PRATICA---------------------------------------
def fatorial(num=1):
    f = 1
    for cont in range(num,0,-1):
        f *= cont
    return f


#PROGRAMA PRINCIPAL --------------------------
n = int(input("Digite um número: "))
print(f'O fatorial de {n} é igual a {fatorial(n)} .')


def par(n=0):
    if n %2 == 0:
        return True
    return False

n = int(input('Digite um número: '))
if par(n):
    print('PAR')
else:
    print('IMPAR')