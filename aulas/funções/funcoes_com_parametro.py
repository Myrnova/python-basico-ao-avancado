"""
Funções com parametros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;


def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

print(quadrado()) # TypeError



def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Marcos')


#? Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
#? em uma função quantos parâmetros forem necessários. Eles são separados por vírgula

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))

print(soma(10, 20))

print(multiplica(10, 20))

print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 5, 4)) # TypeError - Passando argumentos a mais

# print(soma(4)) # TypeError - Passando argumentos a menos


# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

#* A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

#! A ordem dos parâmetros importa!

#* Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(sobrenome='Jolie', nome='Angelina'))


#* Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return total # errado
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

"""
