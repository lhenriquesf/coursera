def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n+2)

def teste():
    for x in range(10):
        print(x)

print(fibonacci(1))