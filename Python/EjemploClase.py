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
