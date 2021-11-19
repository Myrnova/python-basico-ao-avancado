"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por Map(Java) ou Dictionary(C#).

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;



#* Criação de dicionários

# Forma 1 (mais comum)
paises = { 'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai' }

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

#* Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru])
# OBS: Caso tentamos fazer um acesso utilizando uma chave inexistente, teremos KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))

#? Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError
pais = paises.get('ru')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

#? Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')


#* Verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

#* É possível utilizar qualquer tipo de dado int, float, string, boolean, lista, tupla,
#* como chaves de dicionários
localidades = {
    (30.5659, 39.5658): 'Escritório em Tokio',
    (40.5659, 74.5658): 'Escritório em Nova York',
    (37.5659, 122.5658): 'Escritório em São Paulo'
}

#* Adicionar elementos em um dicionário
receita = {
    'jan': 100, 'fev': 120, 'mar': 300
}
# Forma 1 
receita['abr'] = 350
# Forma 2
novo_dado = { 'mai': 500 }
receita.update(novo_dado) # receita.update({ 'mai': 500 })

#* Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
# Forma 2
receita.update({ 'mai': 600 })

#? CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
#? CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas

#* Remover dados de um dicionário
# Forma 1 - Mais comum
receita.pop('mar')
# Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado 
# Ao removermos um objeto, o valor deste objeto é retornado pelo pop

# Forma 2
del receita['fev']
# Se a chave não existir será gerado KeyError


#* Imagine que você tem um comércio eletrônico, onde temos um carrinho de compra na qual adicionamos produtos.
# Com lista
carrinho = []
produto1 = ['Playstation 4', 1, 2030.00]
produto2 = ['God of War 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)

# Com tuplas
carrinho = []
produto1 = 'Playstation 4', 1, 2030.00
produto2 = 'God of War 4', 1, 150.00
carrinho.append(produto1)
carrinho.append(produto2)

# Com dicionário
carrinho = []
produto1 = { 'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2030.00 }
produto2 = { 'nome': 'God of War 4', 'quantidade':1, 'preco': 150.00 }
carrinho.append(produto1)
carrinho.append(produto2)

#* Limpar dicionário
receita.clear()

#* Copiar um dicionário para outro
# Forma 1 - Deep Copy
novo = receita.copy() 
novo['maio'] = 4

# Forma 2 - Shallow Copy
novo = receita
novo['maio'] = 4

#* Forma não usual de criação de dicionários
# O método fromkeys recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a essa chave o valor informado.

outro = {}.fromkeys('a', 'b')
outro = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
veja = {}.fromkeys('teste', 'valor') # {'t': 'valor', 'e': 'valor', 's': 'valor'}, t & e se repetem e dicionário só aceita uma chave de mesmo nome
print(veja)
veja = {}.fromkeys(range(1, 11), 'novo')


#* Iterar sobre dicionários
for chave in receita:
    print(chave)
for chave in receita:
    print(receita[chave])
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

#* Acessando as chaves
for chave in receita.keys():
    print(f'Em {chave} recebi R$ {receita[chave]}')

#* Acessando os valores
for valor in receita.values():
    print(valor)

#* Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
    
#* Soma, Valor Máximo, Valor Mínimo, Tamanho
print(sum(receita.values))
print(max(receita.values))
print(min(receita.values))
print(len(receita))
"""





