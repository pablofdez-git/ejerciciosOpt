# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena
# con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres
# dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input("Introduce el nombre de un producto: ")
precio = float(input("Introduce el precio: "))
unidades = int(input("Introduce el numero de unidades: "))
total = precio * unidades

print()
