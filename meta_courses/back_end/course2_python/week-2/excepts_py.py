import random

filename = 'week-2/petnames.txt'

def read_file(file):
    with open(filename) as f:
            file_content = f.read()
            #print(file_content)
    return file_content

file_contents = read_file(filename)

lista = file_contents.split()
print(lista[0])

lista1 = ['luiz','igor','souza']
ll = []
for x in range(len(lista1)-1,-1,-1):
      ll.append(lista1[x])
print(ll)