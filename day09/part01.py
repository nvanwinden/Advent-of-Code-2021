low_points = []

def check_first_row(rows) :
	i = 0
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[0][i] < rows[0][i+1] and rows[0][i] < rows[1][i]) :
				low_points.append(rows[0][i])
		elif (i == len(rows[0]) - 1) :
			if (rows[0][i] < rows[0][i-1]) and rows[0][i] < rows[1][i] :
				low_points.append(rows[0][i])
		else :
			if (rows[0][i] < rows[0][i-1] and
			rows[0][i] < rows[0][i+1] and
			rows[0][i] < rows[1][i]) :
				low_points.append(rows[0][i]) 
		i += 1

def check_last_row(rows) :
	i = 0
	pos = len(rows) - 1
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[pos][i] < rows[pos][i+1] and rows[pos][i] < rows[pos-1][i]) :
				low_points.append(rows[pos][i])
		elif (i == len(rows[0]) - 1) :
			if (rows[pos][i] < rows[pos][i-1]) and rows[pos][i] < rows[pos-1][i] :
				low_points.append(rows[pos][i])
		else :
			if (rows[pos][i] < rows[pos][i-1] and
			rows[pos][i] < rows[pos][i+1] and
			rows[pos][i] < rows[pos-1][i]) :
				low_points.append(rows[pos][i])
		i += 1

def check_middle_row(rows, pos) :
	i = 0
	while (i < len(rows[0])) :
		if (i == 0) :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and
			rows[pos][i] < rows[pos][i+1]) :
				low_points.append(rows[pos][i])
		elif (i == len(rows[0]) - 1) :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and
			rows[pos][i] < rows[pos][i-1]) :
				low_points.append(rows[pos][i])
		else :
			if (rows[pos][i] < rows[pos-1][i] and
			rows[pos][i] < rows[pos+1][i] and
			rows[pos][i] < rows[pos][i-1] and
			rows[pos][i] < rows[pos][i+1]) :
				low_points.append(rows[pos][i])
		i += 1

f = open('input.txt')
data = f.read()
f.close

data_split = data.split('\n')

rows = []

for row in data_split :
	l = list(row)
	rows.append(l)

lst_len = len(rows)
y = 0

while (y < len(rows)) :
	if (y == 0) :
		check_first_row(rows)
	elif (y == len(rows) - 1) :
		check_last_row(rows)
	else :
		check_middle_row(rows, y)
	y += 1

sum_risk_levels = 0

for point in low_points :
	sum_risk_levels = sum_risk_levels + (int(point)+1)

print(sum_risk_levels)
