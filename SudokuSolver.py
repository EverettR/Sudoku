board = [
    [4,9,8,0,2,0,5,0,0],
    [0,0,0,0,0,0,0,9,0],
    [7,3,0,1,9,4,2,0,0],
    [6,1,2,4,0,0,0,0,5],
    [0,0,0,0,0,6,0,0,0],
    [8,0,9,7,0,0,6,3,2],
    [5,0,0,0,1,0,0,0,9],
    [0,6,1,9,0,0,3,0,0],
    [0,7,3,8,0,0,1,0,0],
    ]


# Prints board in console
def print_board(board):
    for i in range(len(board[0])):
        if i % 3 == 0 and i !=0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") 


# Checks if board is valid for row, column, and square
def valid_board(board, num, pos):

    # Check Row
    for i in range(len(board[0])):
        if board[pos[0][i]] == num and pos[1] !=i:
            return False


def main():
    print_board(board)


if __name__ == "__main__":
    main()
