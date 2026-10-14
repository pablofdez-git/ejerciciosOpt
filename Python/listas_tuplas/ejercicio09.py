
#! 9. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra_user = input("Ingresa una palabra: ").lower()

vocal_a = palabra_user.count('a')
vocal_e = palabra_user.count('e')
vocal_i = palabra_user.count('i')
vocal_o = palabra_user.count('o')
vocal_u = palabra_user.count('u')

print(f"La palabra {palabra_user} contiene:")
print(f"{vocal_a} veces la vocal 'a'")
print(f"{vocal_e} veces la vocal 'e'")
print(f"{vocal_i} veces la vocal 'i'")
print(f"{vocal_o} veces la vocal 'o'")
print(f"{vocal_u} veces la vocal 'u'")
