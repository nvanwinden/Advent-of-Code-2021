def init_fish_count_per_timer(initial_state) :
	days = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for fish in initial_state :
		days[int(fish)] += 1
	return (days)

f = open('input.txt')
data = f.read()
f.close

initial_state = data.split(',')
timer = init_fish_count_per_timer(initial_state)

i = 0
while (i < 256) :
	j = 0
	new_fish = 0
	while (j < len(timer)) :
		if (timer[j] > 0) :
			if (j == 0) :
				new_fish = timer[j]
			else :
				timer[j-1] = timer[j]
			timer[j] = 0
		j += 1
	if (new_fish > 0) :
		timer[6] += new_fish
		timer[8] += new_fish
	i += 1

print(sum(timer))
