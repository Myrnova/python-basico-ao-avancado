"""
Generator Expression

Em aula anteriores nós estudamos
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

# List Comprehension                         

res = [nome[0] == 'C' for nome in nomes]
print(all(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(all(res))

#* Generator ocupa bem menos espaço na memória do que um set, list, dictionary comprehension
ja que não gera instantaneamente o valor e sim apenas quando você utiliza o mesmo em outra parte do código

#* Iterar generator expression
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

"""

