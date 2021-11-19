"""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada.


for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)


"""


while True:
    comando = input('Digite "sair" para sair: ')
    if comando.lower() == 'sair':
        break