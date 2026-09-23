
#/ Variables
#! Ejercicio 1
## a
nombre = "Pablo"
## b
apellido = "Fernandez"
## c
nombreCompleto = nombre, apellido
# d
pais = "España"
# e
ciudad= "Valladolid"
# f
edad = 21
# g
año = 2005
# h
is_married = False
# i
is_true = True
# j
is_light_on = True
# k
direccion, portal, ciudad, codigo_postal = "Av Madrid", 13, "Laguna de Duero", 47140

# Ejercicio 2
print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(direccion))
print(type(portal))
print(type(ciudad))
print(type(codigo_postal))

# Ejercicio 3
print(len(nombre))
print(len(ciudad))


# Ejercicio 4
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
pais = input("Introduce tu pais: ")
edad = input("Introduce tu edad: ")

print("Me llamo", nombre, apellido, "mi pais es", pais, "y tengo", edad, "años")
