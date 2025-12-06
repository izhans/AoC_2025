"""
 * read nums and perform the operation they need
"""

answer = 0

rows = open("input").read().split("\n")
n_rows = len(rows)
row_len = len(rows[0])
ops_row = n_rows -1

res = 0
op = ""

for x in range(row_len):
	n = 0

	if op == "":
		op = rows[ops_row][x]
	if op == "*" and res == 0:
		res = 1

	# interpretar numero
	for y in range(ops_row):
		if rows[y][x] != " ":
			n = n * 10 + int(rows[y][x])

	# resetear para nuevo problema
	if n == 0:
		answer += res
		res = 0
		op = ""
	else:
		if op == "+":
			res += n
		else:
			res *= n

answer += res
print(answer) # 1058 + 3253600 + 625 + 8544 = 3263827