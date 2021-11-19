"""
Listas (lists)

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
    - Dinâmico: Não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elemento;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado

As listas em Python são representadas por colchetes: []

Listas são mutáveis: ou seja, elas podem mudar constantemente


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#* Checar se determinado valor está contido na lista
num = 18

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#* Ordenar uma lista
lista1.sort()

#* Contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#* Adicionar elementos em listas

# Para adicionar elementos em listas, utilizamos a função append
# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez

lista1.append(42, 12, 56) # Erro

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)

lista1.append(42)

lista1.extend([123, 44, 67]) # coloca cada elemento da lista como valor adicional a lista
# Inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial dessa posição, o mesmo será deslocado para a direita da lista.

lista1.insert(2, 'Novo valor')


#* Juntar duas listas
lista6 = lista1 + lista2
lista1.extend(lista2)
lista1 += lista2


#* Inverter uma lista
lista1.reverse()
lista2.reverse()

print(lista1[::-1])
print(lista2[::-1])

#* Copiar uma lista
lista6 = lista2.copy()

#* Contar quantos elementos existem dentro da lista
print(len(lista2))

#* Remover o último elemento de uma lista
# OBS: o pop não somente remove o último elemento, mas também o retorna
lista5.pop()

#* Remover um elemento pelo índice
# OBS: Os elementos a direita deste índice serão deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos um IndexError
lista5.pop(2)

#* Remover todos os elementos
lista5.clear()

#* Repetir elementos uma lista
nova = [1, 2, 3]
nova *= 3

#* Converter string para lista
# OBS: Por padrão o split separa os elementos da string pelo espaço entre as palavras
curso = 'Programação em Python: Essencial'
curso = curso.split()

curso = 'Programação,em,Python:,Essencial'
curso = curso.split(',')


#* Converter lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']

# Pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6) 
curso = '$'.join(lista6)

#* É possível colocar qualquer tipo de dado em uma lista, inclusive misturando os dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45481264516]

#* Iterando sobre listas
#? Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma += elemento
print(soma)

#? Utilizando while
carrinho = []
produto = ''
while produto != 'sair':    
    produto = input("Adicione um produto na lista ou digite 'sair': ")
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
    
#* Acessar os elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


#* Acessar os elementos de forma indexada inversa
#? Para entender melhor o índice negativo, pense na lista como um círculo, 
#? onde o final de um elemento está ligado ao início da lista
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # Erro, pois não existe esse índice

#* Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)



#! Outros métodos não tão importantes, mas também úteis

#* Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice esta o valor 6?
print(numeros.index(6))

# numeros.index(19) # Gera ValueError
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

print(numeros.index(5)) # Retorna o índice do primeiro elementro encontrado

#* Fazer busca dentro de um range, ou seja, qual índice começar a buscar

print(numeros.index(5, 2)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2
print(numeros.index(5, 3)) # buscando a partir do índice 3
# print(numeros.index(5, 4)) # buscando a partir do índice 4 # Gera ValueError

#* Fazer busca dentro de um range, inicio/fim

print(numeros.index(8, 3, 6)) # buscar o indice de valor 8, entre os indices 6 e 8

#* Revisar slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

#* Slice de lista com parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

#* Slice de lista com parâmetro 'fim'

print(lista[:2]) # começa em 0 e vai até o índice 2 sem incluir ele 

#* Slice de lista com parâmetro 'passo'

print(lista[1::2]) # começa em 1, vai até o final de 2 em 2

#* Invertendo valores em uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
nomes.reverse()

#* Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# *Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista


#* Transformar lista em tupla
lista = [1, 2, 3, 4, 5, 6]

tupla = tuple(lista)

print(tupla)

#* Desempacotamento de listas

num1, num2, num3, num4, num5, num6 = lista

print(num1)
print(num3)
print(num2)

# OBS: se tiver um número diferente de elementos na lista ou variávies para receber os dados, teremos ValueError

"""

#* Copiando uma lista para outra (Shallow Copy e Deep Copy)
lista = [1, 2, 3, 4, 5, 6]

#? Deep Copy
nova = lista.copy()
#? Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram
#? totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso é chamado de DeepCopy

print(nova)

nova.append(7)

print(lista)

#? Shallow Copy
nova2 = lista
#? Veja que utilizamos a cópia de atribuição e copiamos os dados da lista para a nova lista, mas após realizarmos
#? modificação em uma das listas, essa modificação se refletiu em ambos as listas. Isso é chamado de ShallowCopy
#? já que a variável não "recebeu" o valor totalmente, e sim o lugar da memória onde está esse valor da lista
#? então ele faz um apontamento para a memória e não que ele realmente recebeu o valor

nova2.append(7)

print(lista)