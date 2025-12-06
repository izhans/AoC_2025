"""
 * Si viviesemos en un mundo feliz, haría:
	products = set()

	for r in ranges.split("\n"):
		r1, r2 = r.split("-")
		products |= set(range(int(r1), int(r2) +1)) # diferencia
 * Pero como con el input no lo aguanta, pues no puedo
"""

answer = 0

file = open("input")
ranges = file.read().split("\n\n")[0]
products = list()

for r in ranges.split("\n"):
	r1, r2 = r.split("-")
	products.append(list([int(r1), int(r2)]))

products.sort()

for i in range(len(products)):
	if i == 0:
		pass
	else:
		if products[i][0] <= products[i-1][1]:
			# esta contenido en el rango anterior
			if products[i][1] <= products[i-1][1]:
				products[i][0] = products[i-1][0]
				products[i][1] = products[i-1][1]
				continue
			# ajustar el limite de abajo para que no duplique
			else:
				products[i][0] = products[i-1][1] +1
		
	answer += products[i][1] - products[i][0] +1

print(answer)
