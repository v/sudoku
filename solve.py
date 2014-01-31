
def read_board():
    board = []
    with open('board') as fh:
        for line in fh.readlines():
            row = list(line.strip())

            board.append(row)

    return board

def check_rows(board):
    for i, row in enumerate(board):
        if not check_row(board, i):
            return False

    return True

def check_cols(board):
    for i in range(len(board)):
        if not check_col(board, i):
            return False

    return True

def check_col(board, num):
    col = []

    for i in range(len(board)):
        col.append(board[i][num])

    nonempty = filter(lambda x: x != '-', col)

    return len(nonempty) == len(set(nonempty))

def check_row(board, i):
    row = board[i]

    nonempty = filter(lambda x: x != '-', row)

    return len(nonempty) == len(set(nonempty))

def check_squares(board):
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            if not check_square(board, i, j):
                return False
    return True

def check_square(board, i, j):
    numbers = []
    for row in range(i, i+3):
        for col in range(j, j+3):
            numbers.append(board[row][col])

    nonempty = filter(lambda x: x != '-', numbers)

    return len(nonempty) == len(set(nonempty))

def solve(board):
    if not check_rows(board):
        return False

    if not check_cols(board):
        return False

    if not check_squares(board):
        return False

    solved = True
    # look for an empty square.
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                solved = False

                # assign a number
                for number in range(1, 10):
                    board[i][j] = str(number)

                    if solve(board):
                        return board
                board[i][j] = '-'
                return False

    if solved:
        return board

def print_board(board):
    for row in board:
        for num in row:
            print num,

        print ""

    print ""


if __name__ == '__main__':
    board = read_board()
    print board

    print check_rows(board)
    print check_cols(board)
    print check_squares(board)

    print_board(solve(board))
