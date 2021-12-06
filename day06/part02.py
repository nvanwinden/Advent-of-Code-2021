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

fish_reset = 0
fish_new = 0

j = 0
while (j < 256) :
	i = 0
	while (i < len(timer)) :
		if (timer[i] > 0) :
			if (i == 0) :
				fish_reset = timer[i]
				fish_new = timer[i]
			else :
				timer[i-1] = timer[i-1] + timer[i]
			timer[i] = 0
		i += 1
	if (fish_reset > 0) :
		timer[6] += fish_reset
		fish_reset = 0
	if (fish_new != 0) :
		timer[8] += fish_new
		fish_new = 0
	j += 1

print(sum(timer))
