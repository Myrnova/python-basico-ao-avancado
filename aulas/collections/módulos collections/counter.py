"""
Módulo Collections - Counter

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-Performance Container Datetype

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido 
com um dicionário, contendo como chave o elemento do interável passado como parâmetro e como valor a quantidade de 
ocorrências desse elemento


from collections import Counter

#? Exemplo 1
# Podemos utilizar qualquer iterável
lista = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 45, 45, 45, 65, 65]
# Utilizando o Counter
# res = Counter(lista)
print(res)

#? Exemplo 2
# Counter({1: 7, 2: 4, 4: 4, 5: 4, 3: 3, 45: 3, 65: 2})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
from collections import Counter

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam rutrum eget justo ut euismod. Fusce facilisis, sapien vitae rhoncus elementum, risus nunc posuere felis, vulputate lobortis ex dui sit amet lorem. Nulla semper non neque quis iaculis. Ut nisi nulla, porttitor vel quam sed, tincidunt ultricies felis. Etiam in aliquam lacus. Pellentesque cursus tortor non ligula viverra semper. Nulla facilisi.
Maecenas id suscipit mauris. Ut convallis lectus ornare enim egestas faucibus. Integer accumsan neque vitae tristique porta. Nunc nec interdum nisi. Nullam quis rutrum enim. Praesent sed libero eget erat fringilla vestibulum vel non lacus. Sed eu tincidunt mauris. Ut quis varius sapien. Nunc lobortis, turpis sodales pretium ultrices, velit neque faucibus magna, sit amet feugiat urna nisi at quam.
Maecenas venenatis nulla quis ligula lacinia, ac cursus massa condimentum. In suscipit nisl eu eros sodales, vel sodales nunc feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pulvinar rutrum velit, sit amet molestie felis placerat vitae. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin efficitur magna eget enim hendrerit, quis placerat nibh dapibus. In sapien magna, porttitor eget pellentesque ut, malesuada nec turpis. Morbi nec tincidunt neque, et bibendum elit. Donec pellentesque aliquet leo, quis malesuada est sodales eget.
Proin ut maximus turpis, sed imperdiet urna. Maecenas vel iaculis ex, non pretium est. Ut eget blandit ex, id consectetur risus. Donec volutpat erat ut elementum pretium. Nunc tempus feugiat feugiat. Nunc placerat orci vitae sodales tincidunt. Quisque rutrum nunc id augue venenatis placerat. Sed iaculis tellus nec convallis pulvinar. Fusce sit amet purus orci. Vivamus non tristique enim.
Nam in enim turpis. Morbi ut felis libero. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer laoreet lorem nec nibh placerat, a sollicitudin urna malesuada. Mauris congue convallis ex, ut ornare mi lacinia in. Nulla facilisi. Aenean ac suscipit nisi. Etiam convallis, metus a tristique semper, libero elit eleifend ligula, ac interdum libero tortor vitae ligula."""

palavras = texto.lower().replace('.', '').replace(',', '').split()

res = Counter(palavras)

print(res)
# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))