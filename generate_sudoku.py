import random
from solve_sudoku import solve_sudoku
from initialize_board import initialize_board

def generate_sudoku(empty_cells=40):
    board = initialize_board()
    fill_board(board)
    remove_cells(board, empty_cells)
    return board

def fill_board(board):
    numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board.copy()):
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def remove_cells(board, count):
    while count > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            count -= 1
