#57

# a = int(input('Digite um número para ser o valor inicial: '))
# b = int(input('Digite um número ser o valor final: '))
# count = 0
# if a > b or a == b:
#     print('Número inválido. O valor de a deve ser menor que o de b.')
#     a = int(input('Digite um número para ser o valor inicial: '))
#     b = int(input('Digite um número ser o valor final: '))
# if a < b: 
#     for num in range(a, b + 1):        
#         primo = True    
#         if num == 1: # numero 1 nao é primo por só possui um divisor, ele mesmo 
#             primo = False
#         for divisor in range(1, num + 1):     
#             if divisor != 1 and num != divisor and num % divisor == 0:
#                 primo = False
#                 break                                                      
#         if primo:    
#             count += 1
 
# print(f'Entre {a} e {b} existem {count} números primos. ')

#58

# a = int(input('Digite um número para ser o valor inicial: '))
# b = int(input('Digite um número ser o valor final: '))
# soma = 0
# if a > b or a == b:
#     print('Número inválido. O valor de a deve ser menor que o de b.')
#     a = int(input('Digite um número para ser o valor inicial: '))
#     b = int(input('Digite um número ser o valor final: '))
# if a < b: 
#     for num in range(a, b + 1):
#         primo = True    
#         if num == 1: 
#             primo = False
#         for divisor in range(2, num):  # todo número é divisivel por 1 e por ele mesmo, então ignore nesse range                     
#             if num % divisor == 0:
#                 primo = False
#                 break                                                      
#         if primo:    
#             soma += num
 
# print(f'A soma dos números primos entre {a} e {b} é {soma}. ')