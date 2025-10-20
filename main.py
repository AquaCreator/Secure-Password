import random

characters = "+-/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
lenght = int(input("inserte la longitud de su contraseña:"))
password = ""

for i in range(lenght):
    password += random.choice(characters)

print("Contraseña:" + password)