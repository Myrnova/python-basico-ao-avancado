"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas.
O sort() só funciona em listas.
Podemos utilziar o sorted() com qualquer iterável

Como o próprio nome diz, sorted() serve para ordenar

#? O sorted não altera o iterável principal, mas sim retorna uma LISTA com os elementos ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
print(numeros)


#* Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor



#* Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
     {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
     {'username': 'carla', 'tweets': ['Eu amo meu gato']},
     {'username': 'jeff', 'tweets': []},
     {'username': 'bob223', 'tweets': [], 'cor': 'amarelo'},
     {'username': 'doggo', 'tweets': ['Eu gosto de cachorro', 'Vou sair hoje']},
     {'username': 'gal', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
]


print(usuarios)

print(sorted(usuarios, key=len, reverse=True))

print(sorted(usuarios, key=lambda usuario: usuario['username']))

print(sorted(usuarios, key=lambda usuario: usuario['tweets']))


musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Musica 2', 'tocou': 2},
    {'titulo': 'Musica 3', 'tocou': 4},
    {'titulo': 'Musica 4', 'tocou': 32},
]

print(sorted(musicas, key=lambda musica: musica['tocou']))

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

"""
