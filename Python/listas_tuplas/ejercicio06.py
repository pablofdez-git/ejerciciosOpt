
#! 6. Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario
#!    la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas
#!    que el usuario tiene que repetir.

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
for i in asignaturas:
    nota = float(input(f"Introduce la nota de {i}: "))
    if nota >= 5:
        asignaturas.remove(i)
print(f"Asignaturas que tienes que repetir: ", asignaturas)
