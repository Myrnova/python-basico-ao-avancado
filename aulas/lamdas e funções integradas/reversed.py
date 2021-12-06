"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas
A função reverse() só funciona em listas.

Ja a função reversed() funciona com qualquer iterável
Sua função é inverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator


lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)

print(type(res))

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Em conjuntos não definimos a ordem dos elementos
# Conjunto
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end ='')


# Podemos fazer o mesmo sem o uso do for

print(''.join(list(reversed('Geek University'))))

# Ja vimos como fazer isso mais fácil com o slice strings

print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também a vimos como fazer isso utilizando o próprio range()

for n in range(9, -1, -1):
    print(n)
"""
