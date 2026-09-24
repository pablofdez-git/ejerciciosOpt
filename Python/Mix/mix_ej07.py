# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión.
capitalInicial = float(input("Introduce la cantidad a invertir: "))
interesAnual = float(input("Introduce el interes anual: "))
numAnios = int(input("Introduce el numero de años: "))

capitalFinal = capitalInicial * (1 + interesAnual)**numAnios
print("El capital final obtenido es de",capitalFinal)
