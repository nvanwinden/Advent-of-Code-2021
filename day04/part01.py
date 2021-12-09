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

print('rows =', rows)
print('cols =', cols)
