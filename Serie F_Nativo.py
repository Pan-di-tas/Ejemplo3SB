#Basicamente el mismo codigo pero subido desde un archivo local

def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Solicitar entrada del usuario
n = int(input("Introduce el número de valores de la serie de Fibonacci que deseas: "))
print(fibonacci(n))