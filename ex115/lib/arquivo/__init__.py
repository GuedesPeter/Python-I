from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve erro na criação do arquivo.')
    else:
        print(f'\033[35mArquivo {nome} criado com sucesso.\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve erro na abertura do arquivo.')

    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve erro ao escrever o arquivo.')
        else:
            print(f'Novo cadastro de {nome} adicionado')
            a.close()