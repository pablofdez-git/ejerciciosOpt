
#! 9. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contrasenia = "1234"

## Forma 1
iguales = False
while iguales == False:
    contrasenia_user = input("Introduce la contraseña: ")
    if contrasenia_user == contrasenia:
        iguales = True
    else:
        print("Contraseña Incorrecta")
print("Contraseña Correcta")

## Forma 2
while contrasenia != contrasenia_user:
    contrasenia_user = input("Cual es la contraseña")
else:
    print("Contraseña verificada")
