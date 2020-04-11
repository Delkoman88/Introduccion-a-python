def fibonacci(n):

    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


n = int(input('Escribe hasta quenúmero se calculará la serie de Fibonacci: '))
for i in range(n+1):
    print(fibonacci(i))