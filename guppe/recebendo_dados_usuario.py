"""
Recebendo dados usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre: 
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'angelina jolie'
- Aspas duplas -> "angelina jolie"
- Aspas simples triplas -> '''angelina jolie''' 
"""
# - Aspas duplas triplas -> """angelina jolie"""


# Entrada de dados

# print("Qual seu nome?") # Input -> Entrada

nome = input("Qual seu nome? ")

# Exemplo de print 'antigo', python 2.x
# print('Boas vindas, %s' % nome)

# Exemplo de print 'moderno', python 3.x
# print('Boas vindas, {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Boas vindas, {nome}')

# print('Qual sua idade?')

idade = int(input('Qual sua idade? '))

# Processamento

# Saída

# Exemplo de print 'antigo', python 2.x
# print('A idade de %s é %s anos' % (nome, idade))

# Exemplo de print 'moderno', python 3.x
# print('A idade de {0} é {1} anos' .format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A idade de {nome} é {idade} anos')

"""
int(idade) -> cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A pessoa {nome} nasceu em {2021 - idade}')