f = open('input.txt')
data = f.read()
f.close

data_split = data.splitlines()

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 1, "]": 2, "}": 3, ">": 4}

open_chars = "([{<"

score_lst = []

for line in data_split :
	chars = []
	corrupted = 0
	score = 0
	for char in line :
		if (char in open_chars) :
			chars.append(char)
		else :
			check = chars.pop()
			if (pairs[check] != char) :
				corrupted = 1
	if (corrupted == 0) :
		chars.reverse()
		for char in chars :
			score = (score * 5) + points[pairs[char]]
		score_lst.append(score)

score_lst.sort()
print(score_lst[int(len(score_lst) / 2)])
