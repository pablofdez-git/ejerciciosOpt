import math
#! 2. El radio de un círculo es 30 metros.
print("===== EJERCICIO 2 =====")
radio = 30

## a. Calcula el área de un círculo y asigna el valor a una variable llamada area_del_circulo.
print("===== EJERCICIO 2 - a =====")
area = math.pi * radio**2
print(area)

## b. Calcula la circunferencia de un círculo y asigna el valor a una variable llamada
##    longitud_circunferencia.
print("===== EJERCICIO 2 - b =====")
longitud_circunferencia = 2 * math.pi * radio
print(longitud_circunferencia)

## c. Para acabar, solicita el radio como entrada del usuario y calcula el área del circulo y la
##    longitud de la circunferencia resultantes.
print("===== EJERCICIO 2 - c =====")
radio_user = int(input("Introduce el radio: "))
area_user = math.pi * radio_user**2
longitud_circunferencia_user = 2 * math.pi * radio_user
print(radio_user)
print(longitud_circunferencia_user)
