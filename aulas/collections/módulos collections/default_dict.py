"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dicionario = {'curso': 'Programação em Ptyhon: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # key error

Default Dict -> Ao criar um dicionário, nós informamos um valor default, podendo utilizar um lambda para isso. 
Este valor será utilizado sempre que não houver valor definido. Caso tentemos acessar uma chave nao existente,
essa chave será criada e o valor default será atribuido

OBS: lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores
"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Ptyhon: Essencial'

dicionario['outro'] # key error no dicionário comum, mas aqui não

print(dicionario)