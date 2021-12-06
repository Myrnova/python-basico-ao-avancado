"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas.

# Função em Python
def funcao(x):
    return 3 * x + 1
print(funcao(4))

# Expressão Lambda
ret = lambda x: 3 * x + 1 
print(ret(4))

#* Podemos ter expressões lambdas com múltiplas entradas
# strip retira qualquer espaço no começo e no final da string
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY        ', 'jones '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambads também

amar = lambda: 'Como não amar Python'

kwargs = lambda **kwargs: print(kwargs)

kwargs(**{'nome': 'Felicity', 'sobrenome': 'Jones'})

# OBS: Se passarmos mais argumentos do que parâmetros esperados, teremos TypeError


autores = ['Isaac Asimov', 'Ray Bradbury', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H.G. Wells', 'Leigh Brackett']

autores.sort(key=lambda autor: autor.split(' ')[-1].lower())
print(autores)


def gerador_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = gerador_funcao_quadratica(2, 3, -5) # está retornando a lambda para a variável teste

print(teste(0))
print(teste(2))
print(teste(3))

print(gerador_funcao_quadratica(3, 0, 1)(2))
"""
