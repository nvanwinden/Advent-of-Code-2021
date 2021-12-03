def binary_to_num(binary) :
	i = 0
	sum = 0
	binary.reverse()
	for bit in binary :
		sum = (int(bit) * 2 ** i) + sum
		i += 1
	return (sum)

def scrubber_rating(data) :
	i = 0
	remainder = data_split.copy()
	tmp = []
	binary = []

	while (i < len(data_split[0])) :
		zero_bit = 0
		one_bit = 0
		for num in remainder :
			if (int(num[i]) == 0) :
				zero_bit += 1
			else :
				one_bit += 1
		if (zero_bit > one_bit) :
			leading_bit = 1
		elif (zero_bit < one_bit) :
			leading_bit = 0
		else :
			leading_bit = 0

		for item in remainder :
			if (int(item[i]) == leading_bit) :
				tmp.append(item)
		remainder.clear()
		remainder = tmp.copy()
		tmp.clear()
		if (len(remainder) == 1) :
			break
		i += 1

	for item in remainder :
		for c in item :
			binary.append(int(c))
	return (binary_to_num(binary))

def oxygen_generator(data) :
	i = 0
	remainder = data_split.copy()
	tmp = []
	binary = []

	while (i < len(data_split[0])) :
		zero_bit = 0
		one_bit = 0
		for num in remainder :
			if (int(num[i]) == 0) :
				zero_bit += 1
			else :
				one_bit += 1
		if (zero_bit > one_bit) :
			leading_bit = 0
		elif (zero_bit < one_bit) :
			leading_bit = 1
		else :
			leading_bit = 1

		for item in remainder :
			if (int(item[i]) == leading_bit) :
				tmp.append(item)
		remainder.clear()
		remainder = tmp.copy()
		tmp.clear()
		if (len(remainder) == 1) :
			break
		i += 1

	for item in remainder :
		for c in item :
			binary.append(int(c))
	return (binary_to_num(binary))

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

print(oxygen_generator(data) * scrubber_rating(data))
