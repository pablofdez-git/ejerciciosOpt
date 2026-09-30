
#! Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#!      Renta: Menos de 10000€ - Tipo impositivo: 5%
#!      Renta: Entre 10000€ y 20000€ - Tipo impositivo: 15%
#!      Renta: Entre 20000€ y 35000€ - Tipo impositivo: 20%
#!      Renta: Entre 35000€ y 60000€ - Tipo impositivo: 30%
#!      Renta: Más de 60000€ - Tipo impositivo: 45%
#! Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta_anual = float(input("Introduce tu renta anual: "))
if renta_anual < 10000:
    print("Tu tipo impositivo es del 5% ")
elif renta_anual >= 10000 and renta_anual < 20000:
    print("Tu tipo impositivo es del 15% ")
elif renta_anual >= 20000 and renta_anual < 35000:
    print("Tu tipo impositivo es del 20%")
elif renta_anual >= 35000 and renta_anual < 60000:
    print("Tu tipo impositivo es del 30%")
else:
    print("Tu tipo impositivo es del 45%")
