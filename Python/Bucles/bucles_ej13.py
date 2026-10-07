
#! 13. Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
palabra_user = ""
## Forma 1
while palabra_user != "salir":
    print(palabra_user)
    palabra_user = input("Introduce una palabra: ")

## Forma 2
while True:
    print(palabra_user)
    palabra_user = input("Introduce una palabra: ")
    if palabra_user == "salir":
        break
