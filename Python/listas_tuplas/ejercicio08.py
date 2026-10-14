
#! 8. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("Introduce una palabra: ")
palabra = palabra.lower()
palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")
