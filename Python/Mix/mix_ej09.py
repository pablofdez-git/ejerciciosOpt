# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido
# a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

cantidadCuenta = float(input("Introduce la cantidad de dinero depositado en la cuenta de ahorros: "))

anio1 = cantidadCuenta * 1.04
anio2 = anio1 * 1.04
anio3 = anio2 * 1.04

print("Ahorros después del primer año:", round(anio1, 2))
print("Ahorros después del segundo año:", round(anio2, 2))
print("Ahorros después del tercer año:", round(anio3, 2))
