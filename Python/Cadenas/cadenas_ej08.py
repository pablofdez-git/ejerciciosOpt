# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla
# el número de euros y el número de céntimos del precio introducido.

precio = input("Introduce el precio en € con dos decimales: ")
aux = precio.split(',')
print("Total de Euros: ", aux[0], " Total en centimos: ", aux[1])
