

'''
Nessa aula, vamos ver como o Python permite tratar erros
e criar respostas a essas exceções.
Aprenda como usar a estrutura try except no Python de uma forma simples.

Exception é a EXCEÇÃO

try (TENTE ALGUMA COISA):

except(SE NÁO,ACONTENCE UMA EXCEÇÃO):

else (SE DEU CERTO): #OPCIONAL

finally (VAI ACONTESCER SE DER CERTO OU ERRADO): #OPCIONAL

>> DENTRO DE UM TRY PODEMOS TER VÁRIOS EXCEPT


'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else: #OPCIONAL
    print(f'O resultado da divisão é {r}.')
finally: #OPCIONAL
    print('Volte sempre.')

