# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por
# pantalla la misma frase, pero con la vocal introducida en mayúscula.

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

frase_modificada = frase.replace(vocal.lower(), vocal.upper())
print("Resultado:", frase_modificada)
