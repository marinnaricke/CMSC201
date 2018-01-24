#File:        proj1.py
#Author:      Marinna Ricketts-Uy
#Date:        11/17/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program is a simple automata game called Conway's Game of Life. 
#             In the game, as time marches on, there are simple rules that govern whether
#             each pixel will be on or off at the next time step.

ALIVE = "A"
DEAD = "."

# startBoard() Creates the new board and adds the alive cells based upon user input
# Input: the rows and columns given from user
# Output: ask the user which row and column to make alive and return the board
def startBoard(rows,cols):
    aliveRow = " "
    #create the list
    board = [[]]*rows
    #start out with all dead cells
    for r in range(rows):
        board[r] = [DEAD]*cols
    #make live cells based upon userInput for row and column
    while aliveRow != "q":
        aliveRow = input("\nPlease enter the row of a cell to turn on (or q to exit): ")
        if (aliveRow != "q") and (int(aliveRow) < rows):
            aliveRow = int(aliveRow)
            aliveCol = int(input("Please enter a column for that cell: "))
            while aliveCol >= cols:
                print("\tThat is not a valid value; please enter a number\n\tbetween 0 and ",cols-1,"inclusive...")
                aliveCol = int(input("\nPlease enter a column for that cell: "))
            board[aliveRow][aliveCol] = ("A")
        elif (aliveRow != "q") and (int(aliveRow) >= rows):
            print("\tThat is not a valid value; please enter a number\n\tbetween 0 and ",rows-1,"inclusive...")
    return board

# getValidBoard() Asks the user for number of rows and columns, then validates the userInput
# Input: no input
# Output: ask the user for the dimension of the board, number of rows
# and number of columns, returns the rows and columns
def getValidBoard():
    numRows = int(input("Please enter number of rows: "))
    while numRows <= 0:
        print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")
        numRows = int(input("Please enter number of rows: "))
    numCols = int(input("Please enter number of columns: "))
    while numCols <= 0:
        print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 1")
        numCols = int(input("Please enter number of columns: "))
    return numRows,numCols
    
# nextIteration() Changes the board depending on which cells are now alive or dead
# Input: the rows, columns and the current board
# Output: no output, returns the newBoard
def nextIteration(row,col,currentBoard):
    newBoard = [[]]*row
    for r in range(row):
        newBoard[r] = [DEAD]*col
    for i in range(row):
        for j in range(col):
            neighbors = 0
            #if current cell is in the top left corner
            if i == 0 and j == 0:
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the bottom left corner
            elif (i == row - 1) and j == 0:
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the bottom right corner
            elif (i == row - 1) and (j == col - 1):
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the top right corner
            elif i == 0 and (j == col - 1):
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE 
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the first column
            elif (j == 0) and (i > 0) and (i != row - 1):
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the last column
            elif (j == col - 1) and (i > 0) and (i != row - 1):
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the first row
            elif (i == 0) and (j > 0) and (j != col - 1):
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the last row
            elif (i == row - 1) and (j > 0) and (j != col - 1):
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
            #if current cell is in the middle section
            else:
                if currentBoard[i-1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i-1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j-1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i+1][j+1] == ALIVE:
                    neighbors = neighbors + 1
                if currentBoard[i][j] == ALIVE:
                    if neighbors == 1:
                        newBoard[i][j] = DEAD
                    elif neighbors == 2 or neighbors == 3:
                        newBoard[i][j] = ALIVE
                    elif neighbors > 3:
                        newBoard[i][j] = DEAD
                if currentBoard[i][j] == DEAD:
                    if neighbors == 3:
                        newBoard[i][j] = ALIVE
                    else:
                        newBoard[i][j] = DEAD
    return newBoard

# printBoard() prints the current board
# Input: The current board
# Output: the board, with its rows and columns
def printBoard(currentBoard):
    #prints the game board
    for row in currentBoard:
        for column in row:
            print(column, end="")
        print(end="\n")
    
def main():
    rows,cols = getValidBoard()
    gameBoard = startBoard(rows,cols)
    numTurns = int(input("\nHow many iterations should I run? "))
    while numTurns < 0:
        print("\tThat is not a valid value; please enter a number\n\tgreater than or equal to 0")
        numTurns = int(input("\nHow many iterations should I run? "))
    print("Starting Board:\n")
    printBoard(gameBoard)
    counter = 0
    while counter != numTurns:
        counter  = counter + 1
        print("\nIteration ",counter, ":")
        gameBoard = nextIteration(rows,cols,gameBoard)
        printBoard(gameBoard)
main()
        
