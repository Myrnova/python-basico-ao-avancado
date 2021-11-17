"""
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Forma gerais:

# Forma 1

range(valor_parada)

OBS: valor_parada não incluso (início padrão 0, e passo de 1 em 1)

for num in range(11):
    print(num)

# Forma 2

range(valor_inicio, valor_parada)

OBS: valor_parada não incluso (início especificado pelo usuário, e passo de 1 em 1)

for num in range(1, 11):
    print(num, end=' ')

# Forma 3

range(valor_inicio, valor_parada, passo)

OBS: valor_parada não incluso (início especificado pelo usuário, e passo especificado pelo usuário)

for num in range(5, 50, 5):
    print(num, end=' ')

# Forma 4(Inversa)

range(valor_inicio, valor_parada, passo)

OBS: valor_parada não incluso (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(10, -1, -1):
    print(num, end=' ')


"""

