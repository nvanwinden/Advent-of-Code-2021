class basins:
	count = 0
	sizes = []

def get_basin_size(caves, y, x) :
	if (caves[y][x] != '9' and caves[y][x] != 'x') :
		caves[y][x] = 'x'
		basins.count = basins.count + 1
		if y > 0:
			get_basin_size(caves,y-1,x)
		if y < len(caves) - 1:
			get_basin_size(caves,y+1,x)
		if x > 0:
			get_basin_size(caves,y,x-1)
		if x < len(caves[0]) - 1:
			get_basin_size(caves,y,x+1)

def check_first_row(rows) :
	i = 0
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[0][i] < rows[0][i+1] and rows[0][i] < rows[1][i]) :
				get_basin_size(rows.copy(), 0, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		elif (i == len(rows[0]) - 1) :
			if (rows[0][i] < rows[0][i-1]) and rows[0][i] < rows[1][i] :
				get_basin_size(rows.copy(), 0, i)
				basins.sizes.append(basins.count)
				basins.count = 0	
		else :
			if (rows[0][i] < rows[0][i-1] and
			rows[0][i] < rows[0][i+1] and
			rows[0][i] < rows[1][i]) :
				get_basin_size(rows.copy(), 0, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		i += 1

def check_last_row(rows) :
	i = 0
	pos = len(rows) - 1
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[pos][i] < rows[pos][i+1] and rows[pos][i] < rows[pos-1][i]) :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		elif (i == len(rows[0]) - 1) :
			if (rows[pos][i] < rows[pos][i-1]) and rows[pos][i] < rows[pos-1][i] :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		else :
			if (rows[pos][i] < rows[pos][i-1] and
			rows[pos][i] < rows[pos][i+1] and
			rows[pos][i] < rows[pos-1][i]) :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		i += 1

def check_middle_row(rows, pos) :
	i = 0
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and
			rows[pos][i] < rows[pos][i+1]) :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		elif (i == len(rows[0]) - 1) :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and rows[pos][i] < rows[pos][i-1]) :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		else :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and
			rows[pos][i] < rows[pos][i-1] and
			rows[pos][i] < rows[pos][i+1]) :
				get_basin_size(rows.copy(), pos, i)
				basins.sizes.append(basins.count)
				basins.count = 0
		i += 1

f = open('input.txt')
data = f.read()
f.close

data_split = data.split('\n')

rows = []

for row in data_split :
	l = list(row)
	rows.append(l)

y = 0

while (y < len(rows)) :
	if (y == 0) :
		check_first_row(rows)
	elif (y == len(rows) - 1) :
		check_last_row(rows)
	else :
		check_middle_row(rows, y)
	y += 1

basins.sizes.sort(reverse=True)
print(int(basins.sizes[0] * int(basins.sizes[1] * int(basins.sizes[2]))))
