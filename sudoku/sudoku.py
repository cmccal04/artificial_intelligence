

# Implement the backtracking algorithm and solve the sudoku puzzle!
def solve(board):
    empty = find_empty(board)
    
    # Base Case: no empty squares left
    if not empty:
        return True
    
    row, col = empty

    for num in range(1, 10):
        if valid_num(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

# Find an empty square on the board, represented by 0
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    # No empty squares
    return None

# Check the constrants for a number in the puzzle
def valid_num(board, num, pos):
    # Check the row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
            
    # Check the column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    # If valid, return true
    return True

# Print the sudoku board with lines separating the boxes
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def main():
    # Represent the sudoku board as a list of lists
    sudoku_board_easy = [
        [6, 0, 8, 7, 0, 2, 1, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 2, 5, 4, 0, 0, 0, 0, 0],
        [7, 0, 1, 0, 8, 0, 4, 0, 5],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [5, 0, 9, 0, 6, 0, 3, 0, 1],
        [0, 0, 0, 0, 0, 6, 7, 5, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 6, 8, 0, 5, 2, 0, 3]
    ]

    sudoku_board_hard = [
        [0, 7, 0, 0, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 6, 1, 0],
        [3, 9, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 9],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [5, 0, 0, 1, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 7, 6],
        [0, 5, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 5, 0],
    ]

    print("Welcome to the Backtracking Sudoku Solver!")
    choice = int(input("Enter 0 for easy, and 1 for hard: "))

    if choice == 0:
        print("You chose the easy board: ")
        print_board(sudoku_board_easy)
        print("Solving...")
        if solve(sudoku_board_easy):
            print("The solved sudoku board is: ")
            print_board(sudoku_board_easy)
    elif choice == 1:
        print("You chose the hard board: ")
        print_board(sudoku_board_hard)
        print("Solving...")
        if solve(sudoku_board_hard):
            print("The solved sudoku board is: ")
            print_board(sudoku_board_hard)

if __name__ == "__main__":
    main()
