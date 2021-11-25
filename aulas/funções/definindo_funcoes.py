"""
Definindo funções

- Funções são pequenos partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muitos uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada

Já utilizamos várias funções desde que iniciamos este curso:
    - print()
    - len()
    - max()
    - min()
    - count()

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não:
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Nest bloco, pode ter ou não retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com  já conhecido dois pontos que é 
utilizado em Python para definir blocos

"""

def diz_oi():
    print('oi')

"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parâmetro de entrada;
4 - Veja que está função não retorna nada;
"""

diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função

Exemplo:

# Errado
diz_oi

# Certo
diz_oi()

# Funciona, mas é preferível que não utilize
diz_oi ()

"""

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()