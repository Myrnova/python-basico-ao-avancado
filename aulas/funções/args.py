"""
Entendendo o *args

 - O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer 
 coisa desde que comece com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definir-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis


# Exemplos
#?
def soma_todos_numeros(nome, email, *args):    
    return sum(args)

print(soma_todos_numeros('Angelina', 'teste@', 4, 6, 9))
print(soma_todos_numeros('Angelina', 'teste@', 4, 6))
print(soma_todos_numeros('Angelina', 'teste@', 4, 6, 9, 7))

#?
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Não tenho certeza quem você é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""

def soma_todos_numeros(*args):    
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador 

print(soma_todos_numeros(*numeros)) 
#* OBS: O asterisco serve para que informemos ao Pythons que estamos passando como 
#* argumento uma coleção de dados. Dessa forma, ele saberá que precisará antes 
#* desempacotar eses dados.