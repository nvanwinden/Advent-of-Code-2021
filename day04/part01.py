class card :
	check_rows = []
	check_cols = []
	won = 0

def sum_card(card, drawn_numbers) :
	return (0)

def check_bingo(num, i, rows, cols) :
	if num in rows[i] :
		card.check_rows[i].append('x')
	if (len(card.check_rows[i]) == 5) :
		card.won = int((i + 1) / 3)
		print(card.won)
		return (1)
	if num in cols[i] :
		card.check_cols[i].append('x')
	if (len(card.check_cols[i]) == 5) :
		card.won = int((i + 1) / 3)
		return (1)

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

f = open('test_input.txt')
data = f.read()
f.close

boards = data.split('\n\n')
drawn_numbers = boards[0].split(',')
boards.remove(boards[0])
board_count = len(boards)
board_split = []

rows = []
cols = []

for board in boards :
	board_split.append(board.split('\n'))

board_split[2].pop()

for board in board_split :
	get_rows(board)
	get_cols(board)

i = 0
while (i < len(cols)) :
	card.check_rows.append([])
	card.check_cols.append([])
	i += 1

for num in drawn_numbers :
	bingo = 0
	i = 0
	while (i < len(cols)) :
		if (check_bingo(num, i, rows, cols)) :
			bingo = 1
			break
		i += 1
	if (bingo == 1) :
		break

sum_card(board_split[card.won - 1], drawn_numbers)
