
#! Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
numA = int(input("Introduce un número: "))
numB = int(input("Introduce otro número: "))

if numB == 0:
    print("No se puede dividir entre 0")
else:
    result = numA / numB
    print("El resultado de la division es:",result)
