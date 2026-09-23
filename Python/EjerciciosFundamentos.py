
#/ Operadores
import math
#! 1. Encuentra la distancia euclidea entre los puntos (2, 3) y (10, 8).
resultado =  math.sqrt((3 - 2)**2+(8 - 10)**2)
print(resultado)

#! 2. El radio de un círculo es 30 metros.
radio = 30
## a. Calcula el área de un círculo y asigna el valor a una variable llamada area_del_circulo.
area = math.pi * radio**2
print(area)
## b. Calcula la circunferencia de un círculo y asigna el valor a una variable llamada
##    longitud_circunferencia.
longitud_circunferencia = 2 * math.pi * radio
print(longitud_circunferencia)
## c. Para acabar, solicita el radio como entrada del usuario y calcula el área del circulo y la
##    longitud de la circunferencia resultantes.
radio_user = input("Introduce el radio: ")
area_user = math.pi * radio_user**2
longitud_circunferencia_user = 2 * math.pi * radio_user
print(radio_user)
print(longitud_circunferencia_user)

#! 3. Escribe un script que solicite al usuario ingresar la base y la altura de un triángulo y calcule el área de este.
base_user = input("Introduce la base: ")
altura_user = input("Introduce la altura ")
area_triangulo = (base_user * altura_user)/2
print(area_triangulo)

#! 4. Escribe un script que solicite al usuario ingresar los lados a, b y c del triángulo y calcule elperímetro de este.
lado_a = input("Introduce el lado a: ")
lado_b = input("Introduce el lado b: ")
lado_c = input("Introduce el lado c: ")
perimetro = lado_a + lado_b + lado_c
print(perimetro)

#! 5. Haya la pendiente y la distancia euclidea entre los puntos (2, 2) y (6, 10).
pendiente = (6 - 10)/(2 - 2)
distancia_euclidea = math.sqrt((2 - 2)**2+(10 - 6)**2)
print(pendiente)
print(distancia_euclidea)

#! 6. Calcula el valor de y en la siguiente ecuación: y = x^2 + 6x + 9. Despues, determina en qué valor de x, y será 0.
valor_x = input("Introduce el valor de x: ")
valor_y = valor_x**2 + 6 * valor_x + 9



#! 11. ¿Cómo se comprueba si un número es par o no con Python?
num = input("Introduce un numero: ")
print("Es par?", num % 2 is 0)

#! 12. Escribe un script que solicite al usuario ingresar las horas y la tarifa por hora y calcule el salario a percibir.
