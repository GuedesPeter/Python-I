
'''
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

'''
#MINHA SOLUÇÃO:


def votar(ano):
    from datetime import date #ESCOPO DE IMPORTAÇÃO
    idade = date.today().year - ano
    if idade >= 18:
       print('VOTO OBRIGATÓRIO')
    elif idade <= 17 and idade >= 16:
        print('VOTO OPCIONAL')
    elif idade <= 15:
        print('VOTO NEGADO')
    print(f'Você tem {idade} anos.')


'''PROGRAMA PRINCIPAL'''
votar(2006)

#-----------------------------------------------
#SOLUÇÃO CURSO EM VIDEO

def voto(ano):
    from datetime import date #ESCOPO DE IMPORTAÇÃO
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos : VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos : VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos : VOTO OBRIGATÓRIO!'




'''PROGRAMA PRINCIPAL'''
print(voto(2004))
print(voto(1991))
votar(2011)