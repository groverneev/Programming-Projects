
n, k = map(int, input().split())
moves = []
for i in range(k):
    moves.append(list(map(int, input().split())))

used_cells = set()
for move in moves:
    used_cells.add(move[0])
    used_cells.add(move[1])
    used_cells.add(move[2])

used_cells = sorted(list(used_cells))
u = len(used_cells)
unused_count = n - u

cell_to_index = {}

for i in range(u):
    cell_to_index[used_cells[i]] = i

move_counts = {}
for move in moves:
    key = (move[0], move[1], move[2])
    if key in move_counts:
        move_counts[key] += 1
    else:
        move_counts[key] = 1

unique_moves = list(move_counts.items())

max_score = 0
count = 0

def check_board(current_board):
    global max_score, count
    if len(current_board) == u:
        score = 0
        for move, cnt in unique_moves:
            xi = cell_to_index[move[0]]
            yi = cell_to_index[move[1]]
            zi = cell_to_index[move[2]]
            if current_board[xi] == "M" and current_board[yi] == "O" and current_board[zi] == "O":
                score += cnt
        if score > max_score:
            max_score = score
            count = 1
        elif score == max_score:
            count += 1
        return
    current_board.append("M")
    check_board(current_board)
    current_board.pop()
    current_board.append("O")
    check_board(current_board)
    current_board.pop()

check_board([])

multiplier = 1
for i in range(unused_count):
    multiplier = multiplier * 2
count = count * multiplier

print(max_score, count)


