def is_safe(board, row, col):
    # Проверяем, не находится ли клетка под боем других ферзей
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row):
    size = len(board)
    if row == size:
        # Все ферзи успешно размещены
        return True

    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1

    return False

def print_board(board):
    size = len(board)
    for row in range(size):
        line = ""
        for col in range(size):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

# Создаем доску размером 8x8
board = [-1] * 8

# Решаем задачу
if solve_n_queens(board, 0):
    print_board(board)
else:
    print("Решение не найдено")