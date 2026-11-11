
#! 3. Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

result = factorial(5)
print(result)
