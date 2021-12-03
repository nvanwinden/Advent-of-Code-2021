def binary_to_num(binary) :
	i = 0
	sum = 0
	binary.reverse()
	for bit in binary :
		sum = (int(bit) * 2 ** i) + sum
		i += 1
	return (sum)

def power_consumption(data) :
	gamma_rate = []
	epsilon_rate = []
	i = 0

	while (i < len(data_split[0])) :
		bit_count = 0
		for num in data :
			if (int(num[i]) == 0) :
				bit_count += 1
		if (bit_count > len(data_split) / 2) :
			gamma_rate.append(0)
			epsilon_rate.append(1)
		else :
			gamma_rate.append(1)
			epsilon_rate.append(0)
		i += 1
	return (binary_to_num(gamma_rate) * binary_to_num(epsilon_rate))

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

print(power_consumption(data_split))
