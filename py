import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
count = ""
cantidad = int(input("cuantos digitos tendra tu contraseña :)"))
for i in range(cantidad):
    letra = random.choice(caracteres)
    count = count + letra
print(count)
