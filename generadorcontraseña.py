import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("ingresa la longitud de tu contraseña"))
contraseña = ""

for i in range (longitud):
    contraseña += random.choice(caracteres)

print("tu contraseña nueva es: ", contraseña)
