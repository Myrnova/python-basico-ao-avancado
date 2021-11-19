"""
Tipo booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:
true, false

Certo:
True, False
"""

ativo = False
logado = True

print(ativo)

# * Operações básicas

"""
# Negação (not):
Fazendo a negação com booleano, caso seja falso o retorno será verdadeiro, caso seja verdadeiro o retorno será falso.
Ou seja, sempre o contrário
"""
print(not ativo)


"""
# Ou (or):
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
Retorna True se um dos valores do or foi verdeiro, se todos forem falsos, retornará False
"""

print(ativo or logado)

"""
# E (and):
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.
"""

print(ativo and logado)
