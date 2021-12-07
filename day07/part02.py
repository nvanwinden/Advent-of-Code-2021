f = open('input.txt')
data = f.read()
f.close

data_split = data.split(',')

num_list = [int(i) for i in data_split]
num_list.sort()

steps = range(1, max(num_list) + 1)
lowest_fuel = 0
pos_fuel = []

for step in steps :
	fuel_count = 0
	res = 0
	for pos in num_list :
		num_steps = abs(step - pos)
		for num in range(1, num_steps + 1) :
			fuel_count = fuel_count + num
	pos_fuel.append(fuel_count)

print(min(pos_fuel))
