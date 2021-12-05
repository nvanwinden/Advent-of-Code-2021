def find_grid_size(data) :
	largest_num = 0
	for pos in data :
		pos_split = pos.split()
		pos_split_1 = pos_split[0].split(',')
		pos_split_2 = pos_split[2].split(',')
		if (int(pos_split_1[0]) > largest_num) :
			largest_num = int(pos_split_1[0])
		if (int(pos_split_1[1]) > largest_num) :
			largest_num = int(pos_split_1[1])
		if (int(pos_split_2[0]) > largest_num) :
			largest_num = int(pos_split_2[0])
		if (int(pos_split_2[1]) > largest_num) :
			largest_num = int(pos_split_2[1])
	return (largest_num)

def check_horizontal(diagram, x1, y1, x2) :
	if (x1 < x2) :
		while (x1 <= x2) :
			diagram[y1][x1] += 1
			x1 += 1
	else :
		while (x1 >= x2) :
			diagram[y1][x1] += 1
			x1 -= 1

def check_vertical(diagram, x1, y1, y2) :
	if (y1 < y2) :
		while (y1 <= y2) :
			diagram[y1][x1] += 1
			y1 += 1
	else :
		while (y1 >= y2) :
			diagram[y1][x1] += 1
			y1 -= 1

def go_up(diagram, x1, y1, x2, steps) :
	if (x1 > x2) : # go left
		while (steps >= 0) :
			diagram[y1][x1] += 1
			y1 = y1 - 1
			x1 = x1 - 1
			steps = steps - 1
	else : # go right
		while (steps >= 0) :
			diagram[y1][x1] += 1
			y1 = y1 - 1
			x1 = x1 + 1
			steps = steps - 1

def go_down(diagram, x1, y1, x2, steps) :
	if (x1 < x2) : # go right
		while (steps >= 0) : 
			diagram[y1][x1] += 1
			y1 = y1 + 1
			x1 = x1 + 1
			steps = steps - 1
	else : # go left
		while (steps >= 0) :
			diagram[y1][x1] += 1
			y1 = y1 + 1
			x1 = x1 - 1
			steps = steps - 1

def check_diagonal(diagram, x1, y1, x2, y2) :
	steps = abs(x1 - x2)
	if (y1 > y2) :
		go_up(diagram, x1, y1, x2, steps)
	else :
		go_down(diagram, x1, y1, x2, steps)

def check_overlap(diagram) :
	count = 0
	for row in diagram :
		for num in row :
			if (num > 1) :
				count +=1
	return (count)

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

size = find_grid_size(data_split) + 1
rows, cols = (size, size)
diagram = [[0 for i in range(cols)] for j in range(rows)]

i = 0

for pos in data_split :
	pos_split = pos.split()
	pos_split_1 = pos_split[0].split(',')
	pos_split_2 = pos_split[2].split(',')	
	
	x1 = int(pos_split_1[0])
	y1 = int(pos_split_1[1])
	x2 = int(pos_split_2[0])
	y2 = int(pos_split_2[1])

	if (y1 == y2) :
		check_horizontal(diagram, x1, y1, x2)
	elif (x1 == x2) :
		check_vertical(diagram, x1, y1, y2)
	else :
		if (abs(x1 - x2) == abs(y1 - y2)) :
			check_diagonal(diagram, x1, y1, x2, y2)

print(check_overlap(diagram))
