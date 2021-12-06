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

i = 0
while (i < 256) :
	j = 0
	while (j < len(timer)) :
		if (timer[j] > 0) :
			if (j == 0) :
				fish_reset = timer[j]
				fish_new = timer[j]
			else :
				timer[j-1] = timer[j]
			timer[j] = 0
		j += 1
	if (fish_reset > 0) :
		timer[6] += fish_reset
		fish_reset = 0
	if (fish_new != 0) :
		timer[8] += fish_new
		fish_new = 0
	i += 1

print(sum(timer))
