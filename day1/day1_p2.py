"""
 * La rueda tiene 100 valores [0-99]
 * Ln gira hacia la izquierda
 * Rn gira hacia la derecha
 * La contraseña es el numero de veces que la rueda pasa por 0
"""

dial = 50
password = 0

with open("input") as file:
	for line in file:
		if line[0] == "L":
			new = (dial - int(line[1:]))
			step = -1
		else:
			new = (dial + int(line[1:]))
			step = 1
		for i in range(dial, new, step):
			if i % 100 == 0:
				password += 1
		dial = new % 100
print(password)	
