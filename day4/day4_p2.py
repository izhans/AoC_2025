"""
 * Check the surroundings of each paper (@) and update if it can be removed
"""

max_surrounds = 4

def valid(papers, i, j, max_i, max_j):
	if papers[i][j] != "@":
		return 0

	rolls = 0
	if i != 0:
		if j != 0 and papers[i -1][j -1] == "@":
			rolls += 1
		if papers[i -1][j] == "@":
			rolls += 1
		if j != max_j and papers[i -1][j +1] == "@":
			rolls += 1
	if j != 0 and papers[i][j -1] == "@":
		rolls += 1
	if j != max_j and papers[i][j +1] == "@":
		rolls += 1
	if i != max_i:
		if j != 0 and papers[i +1][j -1] == "@":
			rolls += 1
		if papers[i +1][j] == "@":
			rolls += 1
		if j != max_j and papers[i +1][j +1] == "@":
			rolls += 1
	return rolls < max_surrounds

answer = 0

file = open("input")
content = file.read()
lines = content.split("\n")

n_lines = len(lines)
n_line = len(lines[0])

while True:
	removed = 0
	
	for i in range(n_lines):
		for j in range(n_line):
			if valid(lines, i, j, n_lines -1, n_line -1):
				removed += 1
				lines[i] = lines[i][:j] + "x" + lines[i][j +1:]
	
	answer += removed
	if removed == 0:
		break

print(answer)
