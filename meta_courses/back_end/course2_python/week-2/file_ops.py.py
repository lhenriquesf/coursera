# LE ARQUIVO
def read_file(file_name):
    try:   
        with open(file_name) as f:
            file_content = f.read()
        return file_content
    except FileNotFoundError:
        print('Arquivo não encontrado')


# TRANSFORMA ARQUIVO NUME LISTA
def read_file_into_list(file_name):
    f_content_list = []
    with open(file_name,'r') as f:
        for line in f:
            f_content_list.append(line)
        return f_content_list


def write_first_line_to_file(file_contents, output_filename):
    try:
        content = file_contents.split('\n')
        with open(output_filename,'w') as f:
            f.write(content[0])
    except AttributeError:
        print('Sem arquivo')


def read_even_numbered_lines(file_name):
    lista = read_file_into_list(file_name)
    new_lista = []
    for i, l in enumerate(lista):
        if i%2 == 0:
            continue
        else:
            new_lista.append(l)
    return new_lista
    

def read_file_in_reverse(file_name):
    lista = read_file_into_list(file_name)
    new_lista = lista[::-1]
    return new_lista

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("/sampletext.txt")
    write_first_line_to_file(file_contents, "online.txt")
    print(read_file_into_list('sampletext.txt'))
    print(read_even_numbered_lines("sampletext.txt"))

if __name__ == "__main__":
    main()