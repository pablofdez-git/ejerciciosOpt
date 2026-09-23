# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico
# con el mismo nombre (la parte delante de @) pero con dominio nuevoDominio.es.

correo = input("Introduce tu correo electronico: ")
aux = correo.split('@')
final = correo.replace(aux[1], "nuevoDominio.es")
print(final)
