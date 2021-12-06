f = open('input.txt')
data = f.read()
f.close

initial_state = data.split(',')
new_state = initial_state.copy()
tmp_state = []
i = 0

while (i < 80) :
	new_fish = 0
	count = 0
	for timer in new_state :
		if (int(timer) > 0) :
			tmp_state.append(int(timer) - 1)
		elif (int(timer == 0)) :
			tmp_state.append(6)
			new_fish = new_fish + 1
	while (new_fish > 0) :
		tmp_state.append(8)
		new_fish = new_fish - 1
	new_state.clear()
	new_state = tmp_state.copy()
	count = len(new_state)
	tmp_state.clear()
	i += 1

print(count)
