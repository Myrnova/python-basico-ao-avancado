"""
**kargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente de *args que coloca os valores extras
em uma dupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma
esses parâmetros em um dicionário

# Exemplo
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")

# OBS: Os parâmetros *args e **kargs não são obrigatórios

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

#* Nas nossas funções, podemos ter (NESTA ORDEM):
 - Parâmetros obrigatórios:
 - *args
 - Parâmetros defalt (não obrigatórios)
 - **kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(18, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(18, 'Felipe', eu='Não', voce='Vai')
minha_funcao(18, 'Carla', 9,4,3, java=False, python=True)



#* Entenda por quê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
# def mostra_info(a, b,*args, instrutor='Geek', **kwargs):
   # return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args = (3,)
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


#* Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes)) 

# Dois asteriscos para desempacotar dicionários

"""

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS: Os nomes das chaves em um dicionário devem ser o mesmo dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3) #TypeError
