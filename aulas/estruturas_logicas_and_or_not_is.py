"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento: 

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor de booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com o segundo
"""

ativo = True
logado = True

if ativo:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta')


# ativo é False? 

print(ativo is False)