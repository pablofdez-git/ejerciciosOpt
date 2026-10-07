
#! 5. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
#!    y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en porcentaje): "))
num_anios = int(input("Introduce el número de años: "))

for i in range(num_anios):
    cantidad = cantidad + (cantidad / interes * 100)
    print(f"Capital obtenido al final del año {i+1}: {cantidad:.2f}")
