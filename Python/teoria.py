#/ ==============================================================================
#/ TEORÍA Y FUNDAMENTOS DE PYTHON
#/ ==============================================================================

#* Comentario de una línea
'''
Esto es un comentario de varias líneas
'''

#/ TIPOS DE DATOS SIMPLES
#-------------------------------------------------------------------------------
## Tipos numéricos:
    #* Enteros (1, 2, 3, -1, -2, -3)
    #* Decimales (1.0, 2.5, -3.14)
    #* Números Complejos (1 + 2j, 3 - 4j)

## Cadenas: pueden ir entre comillas simples o dobles
'Hola mundo'
"Hola mundo"

## Booleanos: Siempre comienzan en mayúscula
True
False

#/ TIPOS DE DATOS COMPUESTOS (CONTENEDORES)
#-------------------------------------------------------------------------------
## Listas: colecciones ordenadas y mutables de elementos
[1, 2, 3, 4, 5]
["manzana", "pera", "naranja"]
["Juan", "perez", 37]   #& Admite diferentes tipos de datos en una misma lista

## Tuplas: colección ordenada de elementos. Inmutable tras su creación
("Lunes", "Martes", "Miércoles")

## Conjuntos (Sets): colección no ordenada de elementos únicos (sin duplicados)
{1, 2, 3, 4, 5}

## Diccionarios: colecciones de pares clave-valor
{
    'nombre': "juan",
    'apellido': "perez",
    'edad': 37,
    'casado': True,
    'nombreHijos': ["juanito", "juanita"],
}

#/ COMPROBACIÓN DE TIPOS DE DATOS
#-------------------------------------------------------------------------------
print(type(10))                 #$ <class 'int'>
print(type("pera"))             #$ <class 'str'>
print(type({1, 2, 3, 4, 5}))    #$ <class 'set'>

#/ TIPADO DE DATOS (TIPADO DINÁMICO Y DÉBIL)
#-------------------------------------------------------------------------------
nombre = "Juan"
edad = 27
print("Nombre:", nombre, "Edad:", edad)     #$ Nombre: Juan Edad: 27
print(type(edad))                           #$ <class 'int'>

nombre = 96
edad = "Maria"
print("Nombre:", nombre, "Edad:", edad)     #$ Nombre: 96 Edad: Maria
print(type(edad))                           #$ <class 'str'>

## Type Hints (Pistas de tipado)
#* Informar del tipo esperado; no restringe la reasignación en tiempo de ejecución
nombre: str = "Juan"
print(nombre)                   #$ Juan
print(type(nombre))             #$ <class 'str'>
nombre = 86
print(nombre)                   #$ 86
print(type(nombre))             #$ <class 'int'>

## Casteo (Conversión de tipos)
#* Conversión mediante funciones integradas

#> int a float
num_int = 10
num_float = float(num_int)
print(num_int)                  #$ 10
print(num_float)                #$ 10.0

#> int a string
string = str(num_int)
print(type(string))             #$ <class 'str'>

#> string a int
otro_int = int("27")
print(otro_int)                 #$ 27

#> string a list (desempaquetado en caracteres)
palabra = "cachibache"
lista = list(palabra)
print(lista)                    #$ ['c', 'a', 'c', 'h', 'i', 'b', 'a', 'c', 'h', 'e']

#/ VARIABLES
#-------------------------------------------------------------------------------
#* Asignación mediante operador '='

#> Declarar y asignar múltiples variables en una sola línea
nombre, apellido, edad, casado = "juan", "Perez", 25, True

#/ ENTRADA Y SALIDA DE DATOS
#-------------------------------------------------------------------------------
## Salida estándar: print()
print("Hola")                                                   #$ Hola
print("Mi primo se llama", nombre, "y tiene", edad, "años")     #$ Mi primo se llama juan y tiene 25 años  #& Concatenación con comas
print("Hola", "Que tal?", "Es jueves", sep="---", end="FIN\n")   #$ Hola---Que tal?---Es juevesFIN  #& Modificando sep y end
print("Buenos dias")                                            #$ Buenos dias

## Entrada estándar: input()
nombre = input("Como te llamas?: ")     #$ Como te llamas?: (espera lo que escriba el usuario)
edad = input("Cuantos años tienes?: ")  #$ Cuantos años tienes?: (espera lo que escriba el usuario)
print(nombre)                           #$ Pablo (lo que haya escrito el usuario)
print(edad)                             #$ 21 (lo que haya escrito el usuario)
print(type(edad))                       #$ <class 'str'> Siempre devuelve tipo str

#> Casteo manual del input
edad = int(edad)        #* Conversión explícita requerida para operar numéricamente
print(type(edad))                       #$ <class 'int'>

#> Casteo directo en la captura
edad = int(input("Cuantos años tienes?: "))     #$ Cuantos años tienes?: (espera lo que escriba el usuario)

#/ OPERADORES
#-------------------------------------------------------------------------------
## Operadores aritméticos
division = 4 / 3        #* División decimal
print(division)         #$ 1.3333333333333333
division = 4 // 3       #* División entera (trunca decimales)
print(division)         #$ 1

resto = 4 % 3           #* Módulo (resto de la división)
print(resto)            #$ 1

potencia = 2 ** 3       #* Exponente
print(potencia)         #$ 8

numA = 8
numB = 56
print(numA + numB)      #$ 64

## Operadores de comparación
print(3 == 5)           #$ False
print(7 > 3)            #$ True

#* Identidad (is / is not compara identidad en memoria, no solo valor)
print(1 is 1)           #$ True
print(4 is 2 * 2)       #$ True
print(4 is 2 * 5)       #$ False
print(1 is not 8)       #$ True

## Operadores lógicos
print(3 < 2 and 8 > 4)  #$ False
print(not 3 == 5)       #$ True
print(True or False)    #$ True

#/ CADENAS DE TEXTO (STRINGS)
#-------------------------------------------------------------------------------
#& En Python no existe tipo char independiente: es un string de longitud 1
#& len() devuelve el número de caracteres

cadena = "Buenos dias"
print(len(cadena))                      #$ 11
print(len('Murcielago'))                #$ 10

## Operaciones básicas
#> Concatenación y repetición
print("Hola " + cadena + " que tal?")   #$ Hola Buenos dias que tal?  #& Requiere gestionar espacios manualmente
#! print("Hola" + 50)                   #$ ERROR: TypeError (str + int no permitido)
print("Hola" + str(50))                 #$ Hola50
print("Hola" * 5)                       #$ HolaHolaHolaHolaHola (repetición)
#! print("Hola" * 5.0)                  #$ ERROR: TypeError (no se puede multiplicar por float)

## Comparación y pertenencia (Código ASCII)
print("mapa" < "moto")                  #$ True (orden lexicográfico ASCII)
print('A' in "Amanecer")                #$ True
print('B' in "Amanecer")                #$ False
print('a' in "Amanecer")                #$ False (case sensitive)
print('ece' in "Amanecer")              #$ True (búsqueda de subcadena)

## Desempaquetado de caracteres
var = "Python"
a, b, c, d, e, f = var
print(a)                                #$ P
print(b)                                #$ y
print(c)                                #$ t
print(d)                                #$ h
print(e)                                #$ o
print(f)                                #$ n

## Formateo de cadenas
nombre, apellido, edad = "Juan", "Perez", 20
print("Mi nombre es %s %s y tengo %d años" % (nombre, apellido, edad))        #$ Mi nombre es Juan Perez y tengo 20 años  #& Formato antiguo C (%)
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))     #$ Mi nombre es Juan Perez y tengo 20 años  #& Método format()
print("Mi nombre es {1} {0} y tengo {2} años".format(nombre, apellido, edad)) #$ Mi nombre es Perez Juan y tengo 20 años  #& format() posicional
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")                #$ Mi nombre es Juan Perez y tengo 20 años  (f-string: más legible y eficiente)

a, b = 5, 3
print("{}/{} = {:.2f}".format(a, b, a / b))                                    #$ 5/3 = 1.67  #& Formateo decimal a 2 cifras

## Indexación y Slicing (Rebanado)
lenguaje = "Python"
primera_letra = lenguaje[0]             #$ Resultado = P
print(primera_letra)                    #$ P

ultima_letra = lenguaje[-1]             #$ Resultado = n (-1 es el último índice)
print(ultima_letra)                     #$ n

bloque = lenguaje[1:3]                  #$ Resultado = yt (índices 1 al 2, 3 excluido)
print(bloque)                           #$ yt

hasta_fin = lenguaje[3:]                #$ Resultado = hon (desde índice 3 hasta el final)
print(hasta_fin)                        #$ hon

#* Sintaxis slice: [inicio:fin:paso]
alternos = lenguaje[0:5:2]              #$ Resultado = Pto (salto de 2 en 2)
print(alternos)                         #$ Pto

invertir = lenguaje[::-1]               #$ Resultado = nohtyP (inversión completa)
print(invertir)                         #$ nohtyP

## Métodos integrados de cadenas
mayusculas = lenguaje.capitalize()      #$ Resultado = Python (primera letra en mayúscula)
print(mayusculas)                       #$ Python

contletras = lenguaje.count("h")        #& count requiere argumento: cuenta ocurrencias
print(contletras)                       #$ 1

frase = "Mi casa es bonita y mi casa es grande"

termia = frase.endswith("grande")       #$ True
print(termia)                           #$ True

str_tab = 'xyz\t12345\tabc'
result = str_tab.expandtabs()           #$ Reemplaza \t por espacios equivalentes
print(result)                           #$ xyz     12345   abc

print(frase.find("es"))                 #$ 8 (índice primera aparición; -1 si no existe)
print(frase.rfind("es"))                #$ 28 (índice última aparición buscando desde el final)

frase = "Casa123"
print(frase.isalnum())                  #$ True (alfanumérico: solo letras y números)

frase = "Casa"
print(frase.isalpha())                  #$ True (solo letras)

frase = "12345"
print(frase.isdecimal())                #$ True (solo caracteres decimales)

frase = "2423"
print(frase.isdigit())                  #$ True (solo dígitos)

frase = "123"
print(frase.isnumeric())                #$ True (caracteres numéricos)

frase = "mi_variable"
print(frase.isidentifier())             #$ True (nombre de variable válido en Python)

frase = "HOLA"
print(frase.islower())                  #$ False (verifica si está todo en minúsculas)

frase = "hola"
print(frase.isupper())                  #$ False (verifica si está todo en mayúsculas)

palabras = ["Mi", "casa", "es", "bonita"]
print(" ".join(palabras))               #$ Mi casa es bonita (une lista con delimitador)

frase = "   Hola   "
print(frase.strip())                    #$ Hola (elimina espacios al inicio y fin)

frase = "Hola mundo"
print(frase.replace("mundo", "Python")) #$ Hola Python (reemplazo de subcadenas)

frase = "Mi casa es bonita"
print(frase.split())                    #$ ['Mi', 'casa', 'es', 'bonita'] (divide en lista por espacios)

frase = "mi casa es bonita"
print(frase.title())                    #$ Mi Casa Es Bonita (mayúscula en cada palabra)

frase = "Hola MUNDO"
resultado = frase.swapcase()            #$ "hOLA mundo" (invierte mayúsculas y minúsculas)
print(resultado)                        #$ hOLA mundo

frase = "Hola mundo"
print(frase.startswith("Hola"))         #$ True (comprueba prefijo)

#/ ESTRUCTURAS DE CONTROL: CONDICIONALES
#-------------------------------------------------------------------------------
## Condicional simple: if
condicion = True
if condicion:
    print("Se ejecuta el if")           #$ Se ejecuta el if

print("Fuera del if")                   #$ Fuera del if

#* Evaluación implícita a boolean (Truthy / Falsy)
valor = 2 * 10
if valor:
    print("Se ejecuta el if")           #$ Se ejecuta el if (valores numéricos != 0 se evalúan como True)

valor = None
if valor:
    print("Se ejecuta el if")           #$ No se imprime nada (None se evalúa como False)

## Condicional alternativo: if - else
if condicion:
    print("Se entro en el if")          #$ Se entro en el if
else:
    print("Se entro en el else")        #$ No se imprime (condicion es True)

## Condicional múltiple: if - elif - else
#* Evalúa ramas secuencialmente; ejecuta solo la primera coincidencia
condicion = 10
if condicion <= 5:
    print("la condicion es menor o igual a 5")                  #$ No se imprime (10 no es <= 5)
elif condicion > 5 and condicion <= 50:
    print("La condicion es mayor que 5 y menor o igual que 50")  #$ La condicion es mayor que 5 y menor o igual que 50
else:
    print("La condicion es mayor a 50")                         #$ No se imprime (ya entró en el elif)

## Evaluación con cadenas
cadena = ""
if cadena:
    print("La cadena no esta vacia")    #$ No se imprime (strings vacíos "" se evalúan como False)

otra_cadena = "hola"
if otra_cadena == "hola":               #$ Comparación directa de contenido
    print("Las cadenas son iguales")    #$ Las cadenas son iguales

if not (otra_cadena == "hola"):         #$ Negación con 'not'
    print("Las cadenas no son iguales") #$ No se imprime (la condición es False)

## Condicionales anidados
condicion = 57
if condicion > 10:
    if condicion % 2 == 0:
        print("El numero es mayor que 10 y par")        #$ No se imprime (57 es impar)
    elif condicion % 2 != 0:
        print("El numero es mayor que 10 e impar")      #$ El numero es mayor que 10 e impar
else:
    print("El numero es menor o igual que 10")          #$ No se imprime (57 > 10)

#/ ESTRUCTURAS DE CONTROL: BUCLES
#-------------------------------------------------------------------------------
## Bucle While
#* Se ejecuta indefinidamente mientras la condición se evalúe a True

condicion = 0
while condicion < 10:
    print(condicion)                    #$ Imprime 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (uno por línea)
    condicion += 1                      #& Modificación requerida para alcanzar condición de parada

#> While con cláusula else
#* Se ejecuta al finalizar el bucle normalmente sin intervención de 'break'
condicion = 0
while condicion < 10:
    print(condicion)                    #$ Imprime 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (uno por línea)
    condicion += 1
else:
    print("La condicion ya no se cumple")   #$ La condicion ya no se cumple

#> Control de flujo: break
condicion = 0
while condicion < 10:
    print(condicion)                    #$ Imprime 0, 1, 2, 3, 4 (uno por línea)
    condicion += 1
    if condicion == 5:
        break                           #* Interrupción forzada del bucle

condicion = 0
while condicion < 10:
    print(condicion)                    #$ Imprime 0, 1, 2, 3, 4 (uno por línea)
    condicion += 1
    if condicion == 5:
        break
else:
    print("La condicion ya no se cumple") #$ No se ejecuta: 'break' anula el bloque else

#> Control de flujo: continue
condicion = 0
while condicion < 10:
    condicion += 1
    if condicion == 5:
        continue                        #* Salta el resto de la iteración actual
    print(condicion)                    #$ Imprime 1, 2, 3, 4, 6, 7, 8, 9, 10 (el 5 se salta)

## Bucle For
#* Itera directamente sobre secuencias iterables (análogo a foreach)
cadena = "Aprender Python"
for letra in cadena:
    print(letra)                        #$ Imprime cada carácter en su línea: A, p, r, e, n, d, e, r, (espacio), P, y, t, h, o, n

#> Detención con if + break
cadena = "Aprender Python"
for letra in cadena:
    print(letra)                        #$ Imprime A, p, r, e, n, d, e, r, (espacio), P (uno por línea)
    if letra == "P":
        break

## Función range(inicio, fin, paso)
#* inicio: incluido | fin: excluido

for i in range(10):                     #$ 1 argumento: define el límite superior (0 a 9)
    print(cadena[i])                    #$ Imprime A, p, r, e, n, d, e, r, (espacio), P (uno por línea)

for i in range(3, 8):                   #$ 2 argumentos: inicio y fin (3 a 7)
    print(cadena[i])                    #$ Imprime e, n, d, e, r (uno por línea)

for i in range(0, len(cadena), 2):      #$ 3 argumentos: inicio, fin y paso incremental
    print(cadena[i])                    #$ Imprime A, r, n, e, (espacio), y, h, n (uno por línea)

#> Recorrido inverso con range()
for i in range(len(cadena) - 1, -1, -1):
    print(cadena[i])                    #$ Imprime n, o, h, t, y, P, (espacio), r, e, d, n, e, r, p, A (uno por línea)

## Sentencia pass
#* Operación nula; marcador de posición para evitar errores de sintaxis en bloques vacíos
for i in range(5):
    pass

## Bucles anidados
for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")   #$ 1 x 1 = 1 / 1 x 2 = 2 / 1 x 3 = 3 / 2 x 1 = 2 / 2 x 2 = 4 / 2 x 3 = 6 (uno por línea)
    print("-----")                      #$ ----- (se imprime al terminar cada vuelta del bucle externo)

#/ ESTRUCTURAS DE DATOS: LISTAS
#-------------------------------------------------------------------------------
#* Secuencia ordenada y mutable de elementos
#* Permite duplicados y elementos de tipos heterogéneos

## Inicialización
lista_uno = []
lista_dos = list()

print(lista_uno)                        #$ []
print(lista_dos)                        #$ []

lista_frutas = ["Manzana", "Pera", "Sandia", "Melon"]
print(lista_frutas)                     #$ ['Manzana', 'Pera', 'Sandia', 'Melon']
lista_frutas = list(("Manzana", "Pera", "Sandia", "Melon"))
print(lista_frutas)                     #$ ['Manzana', 'Pera', 'Sandia', 'Melon']

## Propiedades básicas
print(len(lista_frutas))                #$ 4 (len(): número total de elementos)

lista_personas = ["Pablo", "Fernandez", 1.82, 21]
print(type(lista_personas))             #$ <class 'list'>

## Desempaquetado (Unpacking)
nombre, apellido, altura, edad = lista_personas
print(apellido)                         #$ Fernandez

#! nombre, apellido = lista_personas    #$ ERROR: ValueError (desajuste entre variables y elementos)

#> Acceso selectivo por índices
nombre, estatura = lista_personas[0], lista_personas[2]
print(nombre)                           #$ Pablo
print(estatura)                         #$ 1.82

#> Agrupación con operador de descompresión (*)
#* Captura el resto de elementos en una sublista (solo puede usarse una vez en la asignación)
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *resto, anteultimo, ultimo = lista_numeros
print(primero)                          #$ 1
print(segundo)                          #$ 2
print(resto)                            #$ [3, 4, 5, 6, 7]
print(anteultimo)                       #$ 8
print(ultimo)                           #$ 9

## Acceso y Modificación
print(lista_frutas[1])                  #$ Pera
print(lista_frutas[-1])                 #$ Melon
#! print(lista_frutas[8])               #$ ERROR: IndexError (índice fuera de rango)

lista_personas[3] = 32                  #* Modificación directa por índice
print(lista_personas)                   #$ ['Pablo', 'Fernandez', 1.82, 32]

## Búsqueda y Conteo
esta_presente = "Pera" in lista_frutas   #* Operador 'in' devuelve booleano
print(esta_presente)                    #$ True

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 1, 6]
print(lista_numeros.count(1))           #$ 2 (count(): apariciones del valor especificado)

print(lista_numeros.index(3))           #$ 2 (index(): índice de la primera coincidencia)
#! print(lista_numeros.index(85))       #$ ERROR: ValueError (el elemento no existe)

#> Conversión de iterables a listas
lista_cadena = list("Hola, buenos dias")
print(lista_cadena)                     #$ ['H', 'o', 'l', 'a', ',', ' ', 'b', 'u', 'e', 'n', 'o', 's', ' ', 'd', 'i', 'a', 's']

## Combinación de listas
#> Concatenación con operador '+' (crea nueva lista sin mutar las originales)
lista_frutas_A = ["Manzana", "Pera", "Sandia", "Melon"]
lista_frutas_B = ["Fresa", "Cereza", "Mango"]
lista_concatenada = lista_frutas_A + lista_frutas_B
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango']

#> Extensión in-place con extend() (modifica la lista que invoca)
lista_frutas_A.extend(lista_frutas_B)
print(lista_frutas_A)                   #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango']

## Inserción de elementos
lista_concatenada.append("Kiwi")        #* append(): inserta al final
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango', 'Kiwi']

lista_concatenada.insert(2, "Coco")     #* insert(índice, valor): inserta en posición específica desplazando el resto
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Coco', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango', 'Kiwi']

## Eliminación de elementos
#> remove(valor): elimina por contenido (primera coincidencia encontrada)
lista_concatenada.remove("Coco")
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango', 'Kiwi']
#! lista_concatenada.remove("Coco")     #$ ERROR: ValueError (elemento no presente)

#> pop(índice): elimina por índice y retorna el elemento eliminado
#* Sin parámetros desapila el último elemento (comportamiento LIFO)
lista_concatenada.pop(2)
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Melon', 'Fresa', 'Cereza', 'Mango', 'Kiwi']

#> del: instrucción para eliminar por índice sin retornar valor
del lista_concatenada[2]
print(lista_concatenada)                #$ ['Manzana', 'Pera', 'Fresa', 'Cereza', 'Mango', 'Kiwi']

#> del sobre identificador completo: destruye la variable en memoria
del lista_concatenada
#! print(lista_concatenada)             #$ ERROR: NameError (la variable ya no existe)

#> clear(): vacía todos los elementos dejando la lista intacta
lista_frutas_A.clear()
print(lista_frutas_A)                   #$ []

## Copia y Duplicación
lista_nums = [1, 2, 3, 4, 5]
lista_otra = lista_nums.copy()          #* copy(): crea copia superficial independiente en memoria
print(lista_nums)                       #$ [1, 2, 3, 4, 5]
print(lista_otra)                       #$ [1, 2, 3, 4, 5]

lista_otra.pop()
print(lista_nums)                       #$ [1, 2, 3, 4, 5]
print(lista_otra)                       #$ [1, 2, 3, 4]

## Ordenación e Inversión
lista_nums.reverse()                    #* reverse(): invierte el orden in-place
print(lista_nums)                       #$ [5, 4, 3, 2, 1]

lista_frutas = ["Manzana", "Pera", "Sandia", "Melon", "Fresa", "Cereza", "Mango"]
lista_frutas.sort()                     #* sort(): ordenación in-place (criterio ascendente/alfabético)
print(lista_frutas)                     #$ ['Cereza', 'Fresa', 'Mango', 'Manzana', 'Melon', 'Pera', 'Sandia']

lista_frutas.sort(reverse=True)         #* sort(reverse=True): ordenación in-place descendente
print(lista_frutas)                     #$ ['Sandia', 'Pera', 'Melon', 'Manzana', 'Mango', 'Fresa', 'Cereza']

#> sorted(): devuelve una nueva lista ordenada sin mutar el iterable original
lista_frutas = ["Manzana", "Pera", "Sandia", "Melon", "Fresa", "Cereza", "Mango"]
lista_frutas_ordenada = sorted(lista_frutas)
print(lista_frutas)                     #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango']
print(lista_frutas_ordenada)            #$ ['Cereza', 'Fresa', 'Mango', 'Manzana', 'Melon', 'Pera', 'Sandia']

lista_frutas_orden_inverso = sorted(lista_frutas, reverse=True)
print(lista_frutas)                     #$ ['Manzana', 'Pera', 'Sandia', 'Melon', 'Fresa', 'Cereza', 'Mango']
print(lista_frutas_orden_inverso)       #$ ['Sandia', 'Pera', 'Melon', 'Manzana', 'Mango', 'Fresa', 'Cereza']

## Slicing en listas
lista_trozo = lista_frutas[2:5]         #* Sublista desde índice 2 hasta 4 (5 excluido)
print(lista_trozo)                      #$ ['Sandia', 'Melon', 'Fresa']
