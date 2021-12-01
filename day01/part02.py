def sum_increased(num_list) :
	i = 0
	count = 0
	while (i < len(num_list) - 3) :
		a = sum(num_list[i:i+3])
		b = sum(num_list[i+1:i+4])
		if (b > a) :
			count += 1
		i += 1
	return (count)

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()
num_list = [int(i) for i in data_split]

print(sum_increased(num_list))
