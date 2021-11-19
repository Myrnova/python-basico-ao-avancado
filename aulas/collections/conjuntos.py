"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, nao são indexados;

Conjuntos são bons para se utilizar quando precisamos armazena elementos
mas não nos importamos com a ordenação deles, quando não precisamos se preocupar com chaves,
valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

#* Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos

# OBS: Ao criar um conjunto, caso seja adiciona um valor já existente,
# o mesmo será ignorado sem gerar erros e não fará parte do conjunto

# Forma 2 - Mais comum
s = { 1, 2, 3, 4, 5, 5, 6, 7, 3, 5}

#* Verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

#* Importante lembrar que não temos valores duplicados, não temos ordem

# Aceita valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'Lista: {lista} com {len(lista)} elementos')
# Aceita valores duplicados
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')
# Não aceita valores duplicados
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
# Não aceita valores duplicados
conjunto = set(lista)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#* Assim como todo outro conjunto de Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}

#* Iterar em um set normalmente
for valor in s:
    print(valor)

    
#* Usos interessantes com sets
#? Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu informam manualmente 
#? a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, ja que em uma lista podemos ter repetição e
# adicionar novos elementos

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Agora precisamos saber quantas cidades distintas,ou seja, unicas, temos
# Podemos utilizar o set para isso:
print(len(set(cidades)))

#* Adicionar elementos em um conjunto
s = { 1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro, é ignorado e não é adicionado

#* Remover elementos em um conjunto
# Forma 1
s.remove(3) # Não é indice, informamos o valor a ser removido.
# s.remove(33) # Caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2
s.discard(2)
# s.discard(33) # Caso o valor não seja encontrado nenhum erro é gerado

#* Copiar um conjunto para outro
# Forma 1 - Deep Copy
novo = s.copy()
# Forma 2 - Shallow Copy
novo = s

#* Remover todos os itens
s.clear()


#* Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo studantes do Curso Python e um 
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana','Patricia'}

# Vejam que alguns alunos que estudam Python também estudam Java.


# Precisamos gerar um conjunto com nomes de estudantes únicos
# Forma 1 - Utilizando Union
unicos1 = estudantes_python.union(estudantes_java)

# Forma2 - Utilizando caractere pipe |
unicos2 = estudantes_java | estudantes_python

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando Intersection
ambos1 = estudantes_python.intersection(estudantes_java)

# Forma2 - Utilizando o &
ambos2 = estudantes_java & estudantes_python


# Gerar um conjunto de estudantes que não estao no outro curso

so_python = estudantes_python.difference(estudantes_java)

#* Soma, Valor Máximo, Valor Mínimo, Tamanho

print(sum(s))
print(sum(s))
print(sum(s))
"""

