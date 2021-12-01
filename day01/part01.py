def num_increased(num_list) :
	i = 0
	count = 0
	start = num_list[0]
	for num in num_list :
		if (i > 0) :
			if (num > start):
				count += 1
			start = num
		i += 1
	return (count)

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()
num_list = [int(i) for i in data_split]

print(num_increased(num_list))
