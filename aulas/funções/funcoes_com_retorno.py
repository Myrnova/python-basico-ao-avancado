"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno do pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno do print: {ret_pr}')

OBS: EM Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retoram valores, devem retornar eses valores com a palavra reservado 'return'

OBS: Não precisamos necessariamente criar uma variável, para receber o retorno de uma função. Podemos passar
a execução da função para outras funções.

# Exemplo função

def quadrado_de_7(): 
    return 7 ** 2

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7()}')

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;


def diz_oi()
    print('Estou sendo executado antes do retorno...')
    return 'Oi'
     print('Estou sendo executado depois do retorno...')


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# Vamos criar uma função para jogar uma moeda
from random import random

def joga_moeda():
    # Gera um número pseudo-randomico entre 0 e 1    
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização de retorno, que na verdade não são erros, mas sim codificação desnecessária
def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else:
        return False

print(eh_impar())

"""
