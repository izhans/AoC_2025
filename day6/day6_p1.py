"""
 * get the sum of x cols with y -1 digits
"""

answer = 0
rows = list()

with open("input") as file:
	for line in file:
		line = line.rstrip("\n")

		rows.append(line.split())
		print(rows)

n_cols = len(rows[0])
ops_row = len(rows) -1

print("cols", n_cols, "rows", ops_row)

for x in range(n_cols):
	res = 0

	for y in range(len(rows) -1):

		if rows[ops_row][x] == "+":
			res += int(rows[y][x])
			print("\tres +", res)
		elif res == 0:
			res = int(rows[y][x])
		else:
			res *= int(rows[y][x])
			print("\tres *", res)

	print("res", res)
	answer += res

print(answer) # 33210 + 490 + 4243455 + 401 = 4277556
