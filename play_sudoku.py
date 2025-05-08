from generate_sudoku import generate_sudoku
from print_board import print_board
from solve_sudoku import solve_sudoku

def play_sudoku():
    board = generate_sudoku()
    print("스도쿠 게임을 시작합니다!")
    while True:
        print_board(board)
        try:
            row = int(input("행 번호 (0~8): "))
            col = int(input("열 번호 (0~8): "))
            num = int(input("입력할 숫자 (1~9): "))
        except ValueError:
            print("숫자를 정확히 입력해주세요.")
            continue

        if board[row][col] != 0:
            print("이미 값이 있는 셀입니다. 다시 시도하세요.")
            continue

        board[row][col] = num
        if not solve_sudoku([row[:] for row in board]):
            print("잘못된 숫자입니다! 게임 종료.")
            break

        if all(0 not in row for row in board):
            print("축하합니다! 스도쿠를 완성했습니다.")
            break
