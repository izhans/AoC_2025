"""
 * This solution also works for part 1 :)
"""

answer = 0
n = 12

with open("input") as file:
	for bank in file:
		bats = list(bank[:-1])
		jolt = 0
		end = n-1

		for i in range(n):
			if end != 0:
				max_num = max(bats[:-end])
			else:
				max_num = max(bats) # this is bc bats[:0] returns empty array

			bats = bats[bats.index(max_num) +1:]
			jolt = jolt * 10 + int(max_num)
			end -= 1
		
		answer += jolt

print(answer)
