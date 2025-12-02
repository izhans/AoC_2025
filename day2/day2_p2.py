"""
 * The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
"""

file = open("input")
ranges = file.readline().split(",")
answer = 0

for r in ranges:
	limits = r.split("-")
	for i in range(int(limits[0]), int(limits[1]) +1):
		n = str(i)
		n_len = len(n)

		for j in range(1, n_len // 2 +1):
			if n.count(n[:j]) == (n_len / j):
				answer += i
				break

print(answer)