answer = 0

with open("input") as file:
	for bank in file:
		bank_len = len(bank) -1
		max_jolt = 0
		print(bank[:-1])

		for i in range(bank_len):
			jolt = 0
			first = int(bank[i]) * 10

			if first // 10 < max_jolt // 10:
				continue

			for j in range(i +1, bank_len):
				if first + int(bank[j]) > jolt:
					jolt = first + int(bank[j])
			
			if jolt > max_jolt:
				max_jolt = jolt

		answer += max_jolt

print(answer)
