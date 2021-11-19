"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variávies globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais:
    - Variávies locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, 
    seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável,
nós não colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

"""

numero = 42 # Exemplo de variável global


if numero > 10:
    novo = numero + 10 # A variavél está sendo declarada dentro do bloco do if, portanto é local
    print(novo)