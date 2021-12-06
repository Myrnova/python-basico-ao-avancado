"""
Min e Max

* max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

# Funciona para lista, tuplas, conjuntos e dicionarios
lista = [1, 8, 4, 99, 34, 129]

print(max(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(dicionario.values()))

print(max(3, 34))


#* Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

print(max(4, 67, 54))
print(max('a', 'ac', 'ab'))
print(max('a', 'f', 'c', 'g'))
print(max('Geek University'))

* min() -> Retorna o menor valor em um iterável ou menor de dois ou mais elementos

# Funciona para lista, tuplas, conjuntos e dicionarios
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(min(dicionario))
print(min(dicionario.values()))

print(min(3, 34))


#* Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

print(min(4, 67, 54))
print(min('a', 'ac', 'ab'))
print(min('a', 'f', 'c', 'g'))
print(min('Geek University'))

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# Padrão é a ordem alfábetica
print(max(nomes)) # Tim
print(min(nomes)) # Arya

print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim

"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Musica 2', 'tocou': 2},
    {'titulo': 'Musica 3', 'tocou': 4},
    {'titulo': 'Musica 4', 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprima somento o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])