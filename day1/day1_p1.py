"""
 * La rueda tiene 100 valores [0-99]
 * Ln gira hacia la izquierda
 * Rn gira hacia la derecha
 * La contraseña es el numero de veces que la rueda apunta al 0
"""

dial = 50
password = 0

with open("test") as file:
	for line in file:
		if line[0] == "L":
			dial = (dial - int(line[1:])) % 100
		else:
			dial = (dial + int(line[1:])) % 100
		if dial == 0:
			password+=1

print(password)	
