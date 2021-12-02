def calc_pos(data) :
	h_pos = 0
	depth = 0
	for line in data :
		line_split = line.split()
		if (line_split[0] == "forward") :
			h_pos += int(line_split[1])
		elif (line_split[0] == "up") :
			depth -= int(line_split[1])
		elif (line_split[0] == "down") :
			depth += int(line_split[1])
	return (h_pos * depth)

f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

print(calc_pos(data_split))
