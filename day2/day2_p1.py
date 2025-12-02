"""
 * The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
"""

file = open("test")
ranges = file.readline().split(",")
answer = 0

for r in ranges:
	limits = r.split("-")
	for i in range(int(limits[0]), int(limits[1]) +1):
		n = str(i)
		n_len = len(n)
		if n_len % 2 != 0:
			continue
		elif n[:n_len // 2] == n[n_len // 2:]:
			answer += i

print(answer)