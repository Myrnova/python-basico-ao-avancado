"""
Map

https://www.geeksforgeeks.org/python-map-vs-list-comprehension/
Com map, fazemos mapeamento de valores para função.


import math

def area(r):
     Calcula a área de um círculo com raio 'r'
     return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [22, 5, 7.1, 0.3, 10, 44]
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável.
# Retorna um Map Object
areas = map(area, raios)

print(list(areas))
print(list(areas))
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Ao utilizar a função map(), após a primeira utilização do resultado, ele zera.


#* Para fixar - Map
Temos dados iteráveis:
dados: a1, a2, ...., an
Temos uma função:
Função f(x)
Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função
O map Object: f(a1), f(a2), f(...), f(an)

cidades = [('Berlim', 29), ('Cario', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]
print(cidades)
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

"""

