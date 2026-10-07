
#! 3. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Introduce un número entero positivo: "))
## Forma 1
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(f"{i},",end=" ")

## Forma 2
for i in range(1, numero +1, 2):
    print(f"{i},",end=" ")
