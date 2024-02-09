def if_poli(str):
    str_list = [i for i in str]
    if_poli = False if str_list[0] != str_list[-1] else True
    return if_poli
        
string = 'racecar'

print(if_poli(string))


def find_number(target):
    x = range(100)
    iterations = 0
    left, right = 0, len(x) - 1

    while left <= right:
        iterations+=1
        middle = (left+right)//2
        isNumber = x[middle]

        if target == isNumber:
            print('Iterations:',iterations)
            return middle
        elif target < isNumber:
            right = middle-1
        else:
            left = middle+1
    return -1
    

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n+2)

def teste():
    for x in range(10):
        print(x)

print(fibonacci(-17))