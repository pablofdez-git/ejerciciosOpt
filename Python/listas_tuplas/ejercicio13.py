
#! 13. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

muestra = input("Introduce números separados por comas: ")

numeros = []
for numero in muestra.split(","):
    numeros.append(float(numero))

media = sum(numeros) / len(numeros)

