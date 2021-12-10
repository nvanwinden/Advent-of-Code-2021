f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

open_chars = "([{<"

total = 0

for line in data_split :
	chars = []
	for char in line :
		if (char in open_chars) :
			chars.append(char)
		else :
			check = chars.pop()
			if (pairs[check] != char) :
				total = total + points[char]

print(total)
