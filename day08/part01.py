def check_segments(value, segments) :
	count = 0
	for segment in segments :
		if segment in value :
			count += 1
	if (count == len(segments)) :
		return (1)
	return (0)

f = open('input.txt')
data = f.read()
f.close

data_split = data.split('\n')

times_appear = 0

for line in data_split :
	line_split = line.split('|')
	signal_patterns = line_split[0].split()
	four_digit_output_value = line_split[1].split()
	for pattern in signal_patterns :
		if (len(pattern) == 2) :
			digit_1 = pattern
		elif (len(pattern) == 4) :
			digit_4 = pattern
		elif (len(pattern) == 3) :
			digit_7 = pattern
		elif (len(pattern) == 7) :
			digit_8 = pattern
	for value in four_digit_output_value :
		if (len(value) == 2 and check_segments(value, digit_1)) :
			times_appear += 1
		if (len(value) == 4 and check_segments(value, digit_4)) :
			times_appear += 1
		if (len(value) == 3 and check_segments(value, digit_7)) :
			times_appear += 1
		if (len(value) == 7 and check_segments(value, digit_8)) :
			times_appear += 1	

print(times_appear)
