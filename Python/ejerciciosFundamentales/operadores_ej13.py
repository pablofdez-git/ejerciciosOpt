
#! 13. Escribe un script que solicite al usuario ingresar el número de años de una persona y
#!     determine la cantidad de segundos que ha vivido.

anios = int(input("Introduce tus años: "))
total_seg = anios * 360 * 24 * 60 * 60
print("Has vivido ",total_seg, " segundos")
