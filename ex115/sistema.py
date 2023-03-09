from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'


if not arquivoExiste(arq):
    criarArquivo(arq)

else:
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    resposta = menu(['PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA','SAIR'])
    if resposta == 1:
        #Opção para listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome= input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('\033[36mSaindo do sistema...Até logo.\033[m')
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)

