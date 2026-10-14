# Comentario de una linea
'''
Esto es un comentario de varias lineas
'''

#/ TIPOS DE DATOS SIMPLES
## Tipos numericos:
    # Enteros (1, 2, 3, -1, -2, -3)
    # Decimales (1.0, 2.5, -3.14)
    # Numeros Complejos (1 + 2j, 3 - 4j)

## Cadenas: pueden ir entre comillas simple os dobles
'Hola mundo'
"Hola mundo"

## Booleanos: Siempre comiuenzan en mayuscula
True
False

#/ TIPOS DE DATOS COMPUESTOS (contenendores)
## Lista: colecciones ordenadas de elementos
[1, 2, 3, 4, 5]
["manzana", "pera", "naranja"]
["Juan", "perez", 37]   # admite diferentes tipos de datos en una misma lista

## Tupla: Coleccion ordenada de elementos. una vez creada es INMUTABLE (no se puede modificar)
("Lunes", "Martes", "Miercoles")

## Conjunto: coleccion no ordenada de elementos. No permite elementos repetidos
{1, 2, 3, 4, 5}

## Diccionarios:
{
    'nombre': "juan",
    'apellido': "perez",
    'edad': 37,
    'casado': True,
    'nombreHijos': ["juanito", "juanita"],
}

#/ COMPROBACION DE TIPOS DE DATOS
print(type(10))                 # <class 'int'>
print(type("pera"))             # <class 'str'>
print(type({1, 2, 3, 4, 5}))    # <class 'set'>

#/ TIPADO DE DATOS - tipado devil
nombre = "Juan"
edad = 27
print("Nombre:", nombre, "Edad:", edad)
print(type(edad))
nombre = 96
edad = "Maria"

print("Nombre:", nombre, "Edad:", edad)
print(type(edad))

# 'Forzar' el tipo de un dato - Informar de que quiero que tenga la variable
nombre: str = "Juan"        # El comportamiento es el mismo con/sin la informacion del tipado
print(nombre)
print(type(nombre))
nombre = 86
print(nombre)
print(type(nombre))

# Casteo: permite convertir un tipo de datos a otro si es posible. Se hace mediante funciones integradas
# int a float
num_int = 10
num_float = float(num_int)
print(num_int)
print(num_float)

# int a string
string = str(num_int)
print(type(string))

# string a int
otro_int = int("27")
print(otro_int)

# string en una lista (desempaquetado de listas)
palabra = "cachibache"
lista = list(palabra)
print(lista)

#/ VARIABLES
# Asigancion de variables (uso del operador de asigancion que es "=")

# Declarar y asignar varias variables en una misma linea
nombre, apellido, edad, casado = "juan", "Perez", 25, True

#/ ENTRADA Y SALIDA DE DATOS POR TERMINAL

# Salida de datos por terminal - print()
print("Hola")
print("Mi primo se llama", nombre, "y tiene", edad, "años")     # Concatenar valores mediante ","
print("Hola", "Que tal?", "Es jueves", sep="---", end="FIN")    # Modificar separador y final
print("Buenos dias")

# Entrada de datos por teclado - input()
nombre = input("Como te llamas?:")
edad = input("Cuantos años tienes?: ")
print(nombre)
print(edad)
print(type(edad))       # El valor devuelto siempre es de tipo str

edad = int(edad)        # Es necesario castear los datos para poder operar con ellos
print(type(edad))

# Es posible castear directamente en la peticion de datos -> 4
edad = int(input("Cuantos años tienes?: "))

#/ OPERADORES

## Operadores aritmeticos
division = 4/3
print(division)
division = 4//3
print(division)

resto = 4%3
print(resto)

potencia = 2**3
print(potencia)

numA = 8
numB = 56
print(numA + numB)

## Operadores de comparacion
print(3==5)             #$ False
print(7>3)              #$True

print(1 is 1)
print(4 is 2*2)
print(4 is 2*5)
print(1 is not 8)

## Operadores lógicos
print(3<2 and 8>4)
print(not 3==5)
print(True or False)


#/ CADENAS

#& Se pueden definir entre comillas simples o dobles
#& En python no existe la clase char, es una cadena de longitud = 1

#& len() permite conocer la longitud de una cadena
cadena = "Buenos dias"
print(len(cadena))
print(len('Murcielago'))

# Concatenar cadenas
print("Hola"+cadena+"que tal?")         #$ se debe atender a los espacios
#? print("Hola" + 50)                      #$ ERROR
print("Hola" + str(50))                 #$ Hola50
print("Hola" * 5)                       #$ Devuelve la cadena 5 veces HolaHolaHolaHolaHola
#? print("Hola" * 5.0)                     #$ ERROR

# Uso de operadores lógicos o de comparacion de cadenas -> ASCII
print("mapa"<"moto")                    #$ True. Comprobacion alfabética
print('A' in "Amanecer")                #$ Comprueba si una secuencia se encuentra dentro de una cadena
print('B' in "Amanecer")                #$ False
print('a' in "Amnecer")                 #$ False. Case sesitive
print('ece' in "Amanecer")              #$ True.

# Secuencias de escape


# Desempaquetado de caracteres
var = "Python"
a, b, c, d, e, f = var
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Formateo de cadenas
nombre, apellido, edad = "Juan", "Perez", 20
print("Mi nombre es %s %s y tengo %d años" %(nombre, apellido, edad))
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
print("Mi nombre es {1} {0} y tengo {2} años".format(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")                      #$ Interpolacion de cadenas y es la mas eficiente
a, b = 5,3
print("{}/{} = {:.2f}".format(a, b, a/b))

# Acceso a caracteres por indice
lenguaje = "Python"
primera_letra = lenguaje[0]
print(primera_letra)                  #$ Resultado = P

ultima_letra = lenguaje[-1]           #$ Resultado = n -> -1 = Ultima letra
print(ultima_letra)

bloque = lenguaje[1:3]                #$ Resultado = yt
print(bloque)

hasta_fin = lenguaje[3:]              #$ Resultado = hon
print(hasta_fin)

# Slice - [inicio:fin:paso]
alternos = lenguaje[0:5:2]            #$ Resultado = Pto -> Va saltando de 2 en 2
print(alternos)

invertir = lenguaje[::-1]             #$ Resultado = nohtyP -> Cadena invertida
print(invertir)

# Funciones con cadenas
mayusculas = lenguaje.capitalize()    #$ Resultado = PYTHON
print(mayusculas)

contletras = lenguaje.count()         #$ Resultado = 6
print(contletras)

frase = "Mi casa es bonita y mi casa es grande"

termia = frase.endswith("grande")     #$ Resultado = True -> Termina con la cadena pasada
print(termia)

str = 'xyz\t12345\tabc'
result = str.expandtabs()             #$ Resultado = xyz     12345     abc -> Reemplaza los tabuladores (\t) por espacios
print(result)

print(frase.find("es"))               #$ Resultado 8 -> La posicion anterior a la que busca | -1 si no hay
print(frase.rfind("es"))              #$ Resultado: 28 -> Empieza por el final

frase = "Casa123"
print(frase.isalnum())                #$ Resultado: True -> Solo contiene letras y números | False si contiene otros caracteres

frase = "Casa"
print(frase.isalpha())                #$ Resultado: True -> Solo contiene letras | False si contiene números, espacios o símbolos

frase = "12345"
print(frase.isdecimal())              #$ Resultado: True -> Solo contiene caracteres numericos

frase = "2423"
print(frase.isdigit)                  #$ Resultado: True -> Solo contiene digitos

frase = "123"
print(frase.isnumeric())              #$ Resultado: True -> Contiene caracteres numéricos

frase = "mi_variable"
print(frase.isidentifier())           #$ Resultado: True -> Puede utilizarse como identificador en Python

frase = "HOLA"
print(frase.islower())                #$ Resultado: False -> No está escrita en minúsculas

frase = "hola"
print(frase.isupper())                #$ Resultado: False -> No está escrita en mayúsculas

palabras = ["Mi", "casa", "es", "bonita"]
print(" ".join(palabras))             #$ Resultado: Mi casa es bonita -> Une los elementos usando un espacio

frase = "  Hola  "
print(frase.strip())                  #$ Resultado: Hola -> Elimina espacios al principio y al final

frase = "Hola mundo"
print(frase.replace("mundo", "Python"))   #$ Resultado: Hola Python -> Reemplaza un texto por otro

frase = "Mi casa es bonita"
print(frase.split())                  #$ Resultado: ['Mi', 'casa', 'es', 'bonita'] -> Separa la frase en una lista

frase = "mi casa es bonita"
print(frase.title())                  #$ Resultado: Mi Casa Es Bonita -> Pone la primera letra de cada palabra en mayúscula

frase = "Hola MUNDO"
resultado = frase.swapcase()          #$ Resultado = hOLA mundo -> Cambia mayúsculas por minúsculas y viceversa
print(resultado)

frase = "Hola mundo"
print(frase.startswith("Hola"))       #$ Resultado: True -> Comprueba si empieza por "Hola"


#/ CONDICIONALES

## Condicional if
condicion = True
if condicion:
    print("Se ejecuta el if")

print("Fuera del if")

valor = 2 * 10
if valor:
    print("Se ejecuta el if")       #$ Cuando una codicion tiene valor se ejecuta el if porque se entiende como true

valor = None
if valor:
    print("Se ejecuta el if")       #$ Cuando una condicion es una variable sin valor se entiende que es false

## Condicional if-else
if condicion:
    print("Se entro en el if")
else:
    print("Se entro en el else")

## Condicional if-elif - Permite verificar varias condiciones mutuamente excluyentes entre si
condicion = 10
if (condicion <= 5):
    print("la condicion es menor o igual a 5")
elif (condicion > 5 and condicion <=50):
    print("La condicion es mayor que 5 y menor o igual que 50")
else:
    print("La condicion es mayor a 50")

## Algunos ejemplos con cadenas
cadena = ""
if cadena:
    print("La cadena no esta vacia")        #$ Cadena vacia como condicion se considera false - cualquier otra true

otra_cadena  = "hola"
if otra_cadena == "hola":                   #$ Compara cadenas caracter a caracter
    print("Las cadenas son iguales")

if not (otra_cadena == "hola"):                   #$ Con not se niega la condicion
    print("Las cadenas no son iguales")

## Anidar condicionales - cuidado con las indentaciones
condicion = 57
if condicion > 10:
    if condicion % 2 == 0:
        print("El numero es mayor que 10 y par")
    elif condicion % 2 != 0:
        print("El numero es mayor que 10 e impar")
else:
    print("El numero es menor o igual que 10")

#/ BUCLES

## While - Se ejecuta mientras la condicion sea verdadera
#while True:
#    print("Bucle infinito")

condicion = 0
while condicion < 10:
    print(condicion)
    condicion += 1                      #$ Mofidificar la condicion para que tienda al valor de salida

#? While + else - Se ejecuta el bloque else cuando la condicion deja de cumplirse
condicion = 0
while condicion < 10:
    print(condicion)
    condicion += 1
else:
    print("La condicion ya no se cumple")

#? Break: Permite forzar la salida del bucle
condicion = 0
while condicion < 10:
    print(condicion)
    condicion += 1
    if condicion == 5:
        break

condicion = 0
while condicion < 10:
    print(condicion)
    condicion += 1
    if condicion == 5:
        break
else:
    print("La condicion ya no se cumple")      #$ No se ejecuta porque el bucle se ha interrumpido con break

#? Continue: Permite saltar a la siguiente iteracion del bucle
condicion = 0
while condicion < 10:
    condicion += 1
    if condicion == 5:
        continue
    print(condicion)

## For - Permite iterar sobre una secuencia de elementos - Similar a foreach de java (se utiliza para recorrer estructuras iterables)
cadena  = "Aprender Python"
for letra in cadena:
    print(letra)

#? Para forzar la detencion del bucle es necesario if+break
cadena  = "Aprender Python"
for letra in cadena:
    print(letra)
    if letra == "P":
        break

#? Funcion range() - Permite generar una secuencias a recorrer
# Sintaxis de range es: range(inicio, fin, paso) -> inicio incluido, fin excluido
for i in range(10):                     #$ Con un solo parametro marcamos el fin
    print(cadena[i])

for i in range(3,8):                    #$ Con dos parametros marcamos el inicio y el fin
    print(cadena[i])

for i in range(0, len(cadena), 2):          #$ Con tres parametros marcamos el inicio, el fin y el paso
    print(cadena[i])

#? Bucle for para recorrer ens entido inverso usando range()
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i])

#? Pass: esta instruccion no hace nada, es un marcador de posicion que se usa para indicar que se incluira algo en ese lugar posteriormente. Evita errores de sintaxis en ausencia de llaves
for i in range(5):
    pass

#? Se pueden anidar bucles. Bucle externo + bucle interno
for i in range(1,3):
    for j in range(1,4):
        print(f"{i} x {j} = {i*j}")
    print("-----")

#/ LISTAS

## Coleccion de distintos tipos de datos ORDENADA y MUTABLE. admite repetidos
## en una lista puede haber elementos del mismo tipo o de distintos tipos
## Existen funciones incorporadas en el lenguaje para trabajar con listas

#? Crear una lista
lista_uno = []
lista_dos = list()

print(lista_uno)
print(lista_dos)

#? Añadir elementos a una lista
lista_frutas = ["Manzana", "Pera", "Sandia", "Melon"]
print(lista_frutas)
lista_frutas = list(("Manzana", "Pera", "Sandia", "Melon"))
print(lista_frutas)

#? Conocer el numero de elementos que hay en una lista -> len()
print(len(lista_frutas))

#? Se pueden añadir elementos de diferente tipo a una lista
lista_personas = ["Pablo", "Fernandez", 1.82, 21]
print(type(lista_personas))

#? Desempaquetar elementos de la lista (No es recomendable)
nombre, apellido, altura, edad = lista_personas
print(apellido)

nombre, apellido = lista_personas                                       #$ ERROR - porque hay distinto numero de variables que de elementos en la lista

#? Para desempaquetar solo algunos valores se puede hacer accedientdo por indice
nombre, estatura = lista_personas[0], lista_personas[2]
print(nombre)
print(estatura)

#? Agrupar elementos a la hora de desempaquetarlos (*) - SOLO PUEDE USARSE UNA VEZ
#? (*) toma todos los elementos
lista_numeros = [1,2,3,4,5,6,7,8,9]
primero, segundo, *resto, anteultimo, ultimo = lista_numeros
print(primero)
print(segundo)
print(resto)
print(anteultimo)
print(ultimo)

#? Acceder a los elementos de una lista por indice
print(lista_frutas[1])
print(lista_frutas[-1])
print(lista_frutas[8])                                                  #$ ERROR

#? Modificar el valor de un elemento
lista_personas[3] = 32
print(lista_personas)

#? Comprobar la pertenencia de un elemento a una lista -> in (boolean)
esta_presente = "Pera" in lista_frutas
print(esta_presente)

#? Conocer el numero de apariciones de un elemento en un lista -> count()
lista_numeros = [1,2,3,4,5,6,7,8,1,6]
print(lista_numeros.count(1))

#? Conocer en que indice se encuentra un determinado valor -> index()
#? Si el elemento aparece mas de una vez devuelve el indice de la primera ocurrencia
print(lista_numeros.index(3))
print(lista_numeros.index(85))

#? Pasar a lista cualquier estructura iterable
lista_cadena = list("Hola, buenos dias")
print(lista_cadena)

#? Concatenar dos listas
#? Usando el operador (+) - asigna la concatenacion a otra lista, sin modificar las listas originales
lista_frutas_A = ["Manzana", "Pera", "Sandia", "Melon"]
lista_frutas_B = ["Fresa", "Cereza", "Mango"]
lista_concatenada = lista_frutas_A + lista_frutas_B
print(lista_concatenada)

#? Usando la funcion extend() - la lista invocante pasa a tener sus elementos y los de la lista invocada
lista_frutas_A.extend(lista_frutas_B)
print(lista_frutas_A)

#? Añadir elementos a la lista
#? Añadir un elemento al final de la lista -> append()
lista_concatenada.append("Kiwi")
print(lista_concatenada)

#? Añadir un elemento en una posicion concreta -> insert()
lista_concatenada.insert(2, "Coco")
print(lista_concatenada)

#? Eliminar elementos de una lista
#? Eliminar un elemento de la lista por valor -> remove()
#? Si esta repetido elimina la primera ocurrencia
lista_concatenada.remove("Coco")
print(lista_concatenada)
lista_concatenada.remove("Coco")          #$ ERROR - No existe el elemento en la lista

#? Eliminar un elemento de la lista por indice -> pop() => ESta funcion devuelve el valor del elemento eliminado
#? Si no se indica el indice elimina el ultimo elemento
#? El comportamiento sin indice es muy utilizaqdo para desapilar elementos de una lista y trabajar con ellos
lista_concatenada.pop(2)
print(lista_concatenada)

#? Eliminar elementos por su indice. SIN DEVOLVER NADA - del
del lista_concatenada[2]
print(lista_concatenada)

#? Eliminar una lista completa -> del
del lista_concatenada
print(lista_concatenada)                 #$ ERROR - la lista ya no existe

#? Dejar la lista vacia -> clear()
lista_frutas_A.clear()
print(lista_frutas_A)

#? Copiar una lista creando una nueva -> copy()
lista_nums = [1,2,3,4,5]
lista_otra = lista_nums.copy()
print(lista_nums)
print(lista_otra)

lista_otra.pop()
print(lista_nums)
print(lista_otra)

#? Dar la vuelta a una lista (el indice 0 pasa a ser el ultimo y el ultimo pasa a ser el 0) -> reverse()
lista_nums.reverse()
print(lista_nums)

#? Ordenar los elementos de una lista -> sort()
#? Si no se indica ordena por criterio de ordenacion natural (alfabetico o numerico)
lista_frutas = ["Manzana", "Pera", "Sandia", "Melon", "Fresa", "Cereza", "Mango"]
lista_frutas.sort()
print(lista_frutas)

#? Si se indica otro criterio se modifica la ordenacion natural
lista_frutas.sort(reverse=True)
print(lista_frutas)

#? Ordena una lista sin modificar la lista original (copiando a otra lista) -> sorted()
lista_frutas = ["Manzana", "Pera", "Sandia", "Melon", "Fresa", "Cereza", "Mango"]
lista_frutas_ordenada = sorted(lista_frutas)
print(lista_frutas)
print(lista_frutas_ordenada)

#? Se puede añadir un criterio de ordenacion distinto al natural
lista_frutas_orden_inverso = sorted(lista_frutas, reverse=True)
print(lista_frutas)
print(lista_frutas_orden_inverso)

#? Cortar elementos de una lista -> slice
lista_trozo = lista_frutas[2:5]
print(lista_trozo)
