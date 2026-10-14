
#! 4. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numeros_ganadores = []
for i in range(6):
    numero = int(input(f"Introduce el numero ganador {i+1}: "))
    numeros_ganadores.append(numero)
numeros_ganadores.sort()
print("Los numeros ganadores ordenados de menor a mayor son:", numeros_ganadores)
