"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance
"""

from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionar elemento no deque

deq.append('y') # Adiciona no final

deq.appendleft('k') # Adiciona no começo da lista

# Remover elementos

deq.pop() # Remove do final da lista e retorna o elemento

deq.popleft() # Remove do começo da lista e retorna o elemento