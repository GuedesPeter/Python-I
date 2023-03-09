

'''
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)

'''

def notas(*n,situacao=False):
    """
    >> Função para analizar notas e situação dos alunos
    :param n: Aceita varias notas de alunos
    :param situacao: Retorna um status conforme a média do aluno
    :return: Dicionário contendo as notas e feedback da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if situacao:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r






#PROGRAMA PRINCIPAL

resp = notas(5.5,2.5,8.5,situacao=True)
help(notas)
print(resp)
