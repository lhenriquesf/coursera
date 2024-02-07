num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0
for i, num in enumerate(num_list):
    count += 1
    if num > 45:
        print('Acima de 45:', num)
    if num == 36:
        print('Número encontrado na posição:', i)
        break
    else:
        print('Abaixo de 45:', num)

print(count)
