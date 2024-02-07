from functools import reduce

lista = [1, 2, 3, 4, 5]

soma = reduce(lambda x, y: x + y, lista)
print(soma)
