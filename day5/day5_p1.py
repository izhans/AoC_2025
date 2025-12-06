"""
 * Check if product id is in any of the ranges
"""

answer = 0

file = open("input")
ranges, products = file.read().split("\n\n")


def is_in_range(p):
	for rang in ranges.split("\n"):
		r = (rang.split("-"))

		if (int(r[0]) <= int(p) <= int(r[1])):
			print(p, r[0], "-", r[1])
			return True
	return False

for p in products.split("\n"):
	if is_in_range(p):
		answer += 1

print(answer)
