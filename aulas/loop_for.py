"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas de repetição

C ou Java
for(int i = 0; i < 10; i ++){
     // execucao loop
}

Python
for item in interavel:
    // execucao loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
    - String
        nome = 'Geek University'
    - Lista
        lista =[1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)

    range(valor_inicial, valor_final)
    OBS: o valor final não é incluso
"""

nome = 'Geek University'
lista =[1, 3, 5, 7, 9]
numeros = range(1, 10)

# Iterando sobre uma string
for letra in nome:
    print(letra)

# Iterando sobre uma lista
for numero in lista:
    print(numero)

#Iterando sobre um range
for numero in numeros:
    print(numero)


"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):     
    print(letra)

OBS: quando não precisamos de um valor, podemos descartá-lo utilizando o underline (_)

for _, letra in enumerate(nome):
    print(letra, end=' ')

qtd = int(input('Quantas vezes esse loop deve rodar? '))

soma_numeros = 0

for n in range(1, qtd + 1)
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma dos números informados é {soma}')
"""
for _, letra in enumerate(nome):
    print(letra, end=' ')
