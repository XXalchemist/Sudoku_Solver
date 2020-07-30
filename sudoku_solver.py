'''
Sudoku Solver - Solve given sudoku that is provides right value to the blank position in the sudoku.
'''

# Input as Sudoku Board

board = [
    [7, 8, '-', 4, '-', '-', 1, 2, '-'],
    [6, '-', '-', '-', 7, 5, '-', '-', 9],
    ['-', '-', '-', 6, '-', 1, '-', 7, 8],
    ['-', '-', 7, '-', 4, '-', 2, 6, '-'],
    ['-', '-', 1, '-', 5, '-', 9, 3, '-'],
    [9, '-', 4, '-', 6, '-', '-', '-', '-'],
    ['-', 7, '-', 3, '-', '-', '-', 1, 2],
    [1, 2, '-', '-', '-', 7, 4, '-', '-'],
    ['-', 4, 9, 2, '-', 6, '-', '-', 7]
]

# Showing board to the user

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print('***********************')

        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print('|', end=' ')
        
        # Printing Numbers        
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end ='')

print_board(board)            

# To find empty positions in given sudoku board

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if b[i][j] == '-':
                return (i,j) # (row,col)