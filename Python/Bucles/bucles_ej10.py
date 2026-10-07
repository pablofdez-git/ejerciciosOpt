
#! 10. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero = int(input("Introduce un numero entero: "))
if numero < 2:
    es_primo = False
else:
    es_primo = True

for divisor in range(2, numero):
	if numero % divisor == 0:
		es_primo = False

if es_primo:
	print("Es un numero primo")
else:
	print("No es un numero primo")
