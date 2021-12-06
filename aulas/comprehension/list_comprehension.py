"""
List Comprehension

 - Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de 
 outro iterável

#* Sintaxe de List Comprehension
[ dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros] 
# lembra map do javascript, pega uma lista, aplica uma função em cima e retorna uma nova com os resultados

print(res)

#* Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
 - A primeira parte: for numero in numeros
 - A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


#* List Comprehension versos Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])



#* Outros exemplos

# 1 
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2 
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, '3.14']])

# 5 
print([str(numero) for numero in [1, 2, 3, 4, 5]])


#* Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
# Exemplos
# 1 
numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares, impares)

# Refatorar

# Qualquer número par utilizando módulo de 2 o resultado é 0 e 0 em Python é False e not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer número impar utilizando módulo de 2 o resultado é 1 e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares, impares)

# 2 
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
"""
