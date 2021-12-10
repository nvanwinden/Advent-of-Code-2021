class card :
	board_count = 0
	check_rows = []
	check_cols = []
	nums_checked = []
	last_called = 0
	won = 0
	boards_won = []

def sum_card(card_won, drawn_numbers) :
	sum_card = 0
	idx = drawn_numbers.index(card.last_called)
	called_nbrs = drawn_numbers[0:idx+1]
	for row in card_won :
		row_split = row.split()
		for num in row_split :
			if num not in called_nbrs :
				sum_card = sum_card + int(num)
	return (sum_card * int(card.last_called))

def check_bingo(num, i, rows, cols) :
	j = 0
	if num in rows[i] :
		card.check_rows[i].append('x')
	if num in cols[i] :
		card.check_cols[i].append('x')
	if (len(card.check_rows[i]) == 5 or len(card.check_cols[i]) == 5) :
		card.won = 0
		while (j < i + 1) :
			j += 5
			card.won += 1
		if (card.won not in card.boards_won) :
			if (len(card.boards_won) == card.board_count - 1) :
				return (1)
			card.boards_won.append(card.won)
		card.last_called = num
		return (0)

def get_rows(board) :
	for row in board :
		rows.append(row.split())

def get_cols(board) :
	i = 0
	col = []
	while (i < len(board)) :
		for row in board :
			row = row.split()
			col.append(row[i])
		cols.append(col)
		col = []
		i += 1

f = open('input.txt')
data = f.read()
f.close

boards = data.split('\n\n')
drawn_numbers = boards[0].split(',')
boards.remove(boards[0])
board_split = []

rows = []
cols = []

for board in boards :
	board_split.append(board.split('\n'))

board_split[len(board_split) - 1].pop()
card.board_count = len(board_split)

for board in board_split :
	get_rows(board)
	get_cols(board)

i = 0
while (i < len(cols)) :
	card.check_rows.append([])
	card.check_cols.append([])
	i += 1

for num in drawn_numbers :
	last_to_win = 0
	i = 0
	while (i < len(cols)) :
		if (check_bingo(num, i, rows, cols)) :
			last_to_win = 1
			break
		i += 1
	if (last_to_win == 1) :
		break

print(sum_card(board_split[card.won - 1], drawn_numbers))
