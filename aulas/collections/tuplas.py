"""
Tuplas (tuple)

Tuplas são bastantes parecidas com listas.

Existem duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda.
Toda operação com uma tupla gera uma nova tupla.

#? CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)

tupla2 = 1, 2, 3, 4, 5, 6

#? CUIDADO 2: Tuplas com 1 elemento

tupla3 = (1) # Isso não é uma tupla!

tupla4 = (1,) # Isso é uma tupla!

#? CONCLUSÃO: Podemos concluir que duplas são definidas pela vírgula e não pelo uso de parênteses

(4) -> Não é tupla
(4,) -> É tuplas
4, -> É tuplas


#* Gerar tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))

#* Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
#? OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

#! Métodos para adição e remoção nas tuplas não existem, dado o fato das tuplas serem imutáveis.

#* Soma-, Valor Máximo-, Valor Mínimo- e Tamanho
# - Se os valores forem todos inteiros ou reais
tupla1 = (1, 2, 3, 4, 5, 6)
print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

#* Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1 + tupla2)
tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores

#* Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

#* Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for index, valor in enumerate(tupla):
    print(index, valor)

#* Contar elementos dentro de uma tupla
tupla = (1, 2, 3, 1, 1, 3, 4)
print(tupla.count(1))


#* O acesso a elementos de uma tupla é igual a de uma lista
print(tupla[5])

#* Iterar com while
i = 0
while i < len(tupla):
    print(tupla[i])
    i += 1


#* Verificar em qual índice um elemento está na tupla
print(tupla.index(1))
#? OBS: Caso o elemento não exista, será gerado ValueError

#* Slicing
# tupla[inicio:fim:passo]
print(tupla[2:])

#* Dicas na utilização de tuplas
#? Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

#* Por quê utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro. Porque trabalhar com elementos imutáveis traz segurança para o código.
"""
