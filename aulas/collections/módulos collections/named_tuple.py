"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple


# Recap tupla
tupla = 1, 2, 3

Named Tuple -> São tupla diferenciadas, onde especificamos um nome para a mesma e também parâmetros

"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca='Chow-chow', nome='Ray')

print(ray)

print(ray[0]) # idade
print(ray.idade)