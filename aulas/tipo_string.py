"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas ->  "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas ->  '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas ->  """uma string""", """234""", """a""", """True""", """42.3"""

"""
print(nome.upper())
print(nome.lower())
print(nome.split()) # transforma em uma lista de strings

"""

nome = 'Geek University'
 
print(nome[0:4]) # selecionando do 0 ao 3, lembrando que nao pega a letra na posição exata de 4

"""
[::-1] -> comece do primeiro elemento, vá até o último elemento e inverta(-1)
"""
print(nome[::-1]) # Inversão de String Pythonico

print(nome.replace('G', 'P'))