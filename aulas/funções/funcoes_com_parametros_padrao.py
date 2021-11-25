"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro é opcional

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError


def exponencial(numero, potencia = 2):
    return numero ** potencia

print(exponencial(2, 3))

#* OBS: 
# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro número, e será calculado o quadrado deste número;
# Se o usuário passar 2 argumentos, este será atribuído ao parâmetro número e o segundo ao parâmetro potencia. Então será calculada a potência

#* OBS: Em funções Python, os parâmetros com valores default(padrão) DEVEM sempre estar ao final da declaração
# ERRO!
def teste(num=2, potencia):
    return num ** potencia

def mostra_informacao(nome = 'Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era instrutor'
    return f'Olá {nome}'

print(mostra_informacao(instrutor=True))
print(mostra_informacao())
print(mostra_informacao('Ozzy'))


#* Por quê utilizar parâmetros com valor default?
 - Nos permite ser mais flexíveis nas funções;
 - Evita erros com parâmetros incorretos;
 - Nos permite trabalhar com exemplos mais legíveis de código;

 
#* Quais tipos de dados podemos utilizar como valores default para parâmetros?
 - Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Valor default sendo função
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, func = soma):
    return func(num1, num2)

def subtracao(num1, num2):
    return num1 - num2    

print(mat(2, 3))
print(mat(2, 2, subtracao))


#* Escopo - Evitar problemas e confusões
# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())
print(instrutor)

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.
# E não substituirá o valor da variável global

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Oi {prof}'

print(diz_oi())
print(prof) # NameError

#? ATENÇÃO com variáveis globais (Se puder evitar, evite!)
#! Não funciona
total = 0
def incrementa():
    total += 1 #UnboundLocalError( A variável local está sendo utilizada para processamento ser ter sido utilizada)
    return total
print(incrementa())
#* Funciona
total = 0
def incrementa():
    global total # Avisando que queremos utilziar a variável global
    total += 1 
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial 
# de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()