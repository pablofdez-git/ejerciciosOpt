
#! 8. Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el siguiente.
#!  1
#!  3 1
#!  5 3 1
#!  7 5 3 1
#!  9 7 5 3 1

num = int(input("Dime un numero: "))
numPira = 1

for i in range(num):
    for j in range(0, i):
        if(j!=0):
            numPira = numPira - 2

        print(numPira, end=" ")

    numPira = numPira+(2*i)
    print("")
