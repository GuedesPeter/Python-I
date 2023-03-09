

'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
 Ex:
 escreva(‘Olá, Mundo!’) Saída:
 ~~~~~~~~~
 Olá, Mundo!
 ~~~~~~~~~
'''
#MINHA SOLUÇÃO
def escreva(texto):
    print('-'*len(texto))
    print(texto)
    print('-' * len(texto))


#--------PROGRAMA PRINCIPAL----------

escreva('CURSO EM VÍDEO')
escreva('PYTHON')
escreva('APRENDA PROGRAMAÇÃO')
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('Olá, Mundo!')

#SOLUÇÃO CURSO EM VIDEO
def escrever(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f' {msg}')
    print('~' * tam)


#--------PROGRAMA PRINCIPAL----------

escrever('CURSO EM VÍDEO')
escrever('PYTHON')
escrever('APRENDA PROGRAMAÇÃO')
escrever('Gustavo Guanabara')
escrever('Curso de Python no YouTube')
escrever('Olá, Mundo!')
