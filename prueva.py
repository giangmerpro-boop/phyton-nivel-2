import random
caracteres = "+-/*!&#?=@abcdefghijklnopqrstuvwxyz"

longitud = int(input("ingresa la longitud: "))

clave = ""

for i in range(longitud):
    caracter = random.choice(caracteres)
    clave += caracter

print("Contraseña generada:", clave)
