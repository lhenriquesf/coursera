# def get_nested_dict_attr_value(tag: Tag, attr: str):
#     attr_dict = {}
#     if hasattr(tag, 'children'):
#         for subtag in tag.children:
#             if hasattr(subtag, 'attrs') and attr in subtag.attrs:
#                 classes = " ".join(subtag.attrs[attr])
#                 attr_dict[classes] = subtag.get_text()
#             attr_dict.update(get_nested_dict_attr_value(subtag, attr))
#     return attr_dict


# def find_factorial_by_loop(n):
#     if n<0:
#         return n
#     else:
#         factorial = 1
#         for i in range(1,n+1):
#             factorial*=i
#         return factorial
    

def find_factorial_recursion(n):
    if n==1:
        return 1
    else:
        return n * find_factorial_recursion(n-1)
    

def str_reverse_recursion(string):
    if len(string) == 0:
        return string
    else:
        return str_reverse_recursion(string[1:]) + string[0]


def str_reverse_simple(string):
    return string[::-1]

