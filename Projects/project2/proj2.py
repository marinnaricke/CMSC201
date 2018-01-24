#File:        proj2.py
#Author:      Marinna Ricketts-Uy
#Date:        12/8/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program implements a tool called "Auto-fill".
#             The program brings in a text file from the user and then asks 
#             the user to provide a point in the grid and will "fill" the entire
#             space it belongs to using a character, also provided by the user.

    
# printBoard() prints the current board
# Input: the currentBoard
# Output: the currentBoard
def printBoard(currentBoard):
    
    for row in currentBoard:
        for column in row:
            print(column,end="")
        print(end = "\n")

# checkInput() checks to see if the coordinate(row,col) given by user is valid
# Input: the coordinate input, rows of the grid, columns of the grid
# Output: asks the user for a different coordinate if its not valid
def checkInput(userInput,rows,columns):
    
    row,col = userInput.split(",")

    while (int(row) < 0 or int(row) > rows - 1) or (int(col) < 0 or int(col) > columns - 1):
        if (int(row) < 0) or (int(row) > rows - 1):
            print("\t",row,"is not a valid row value; please enter a number\n\tbetween 0 and",rows-1,"inclusive.")
        if (int(col) < 0) or (int(col) > columns - 1):
            print("\t",col,"is not a valid column value; please enter a number\n\tbetween 0 and",columns-1,"inclusive.")
        userInput = input("Please enter the coordinates you would like to fill at \n\tin the form \"row,col\": ")
        row,col = userInput.split(",")
    
    row = int(row)
    col = int(col)

    return row,col    

# autoFill() fills in the space surrounding the coordinate given by the user
# Input: the user's answer of yes or no, character choosen by user, the 
#        current board, the row and col coordinate given by user
# Output: if the user answered "yes" to seeing the recursive steps,
#         then the function prints out the board during each step.
def autoFill(userAns,character,currentBoard,row,col):

    #if all neighboring cells are filled, go back to main
    if currentBoard[row-1][col] != (" ") and currentBoard[row][col+1] != (" ") and currentBoard[row+1][col] != (" ") and currentBoard[row][col-1] != (" "):
        return
    else:

        #if the cell above the current cell is unoccupied,
        #fill in the cell w/ the character
        if currentBoard[row-1][col] == (" "):
            currentBoard[row-1][col] = character
            #if user wants to see recursive step, print the board
            if userAns == "yes":
                printBoard(currentBoard)
            autoFill(userAns,character,currentBoard,row-1,col)

        #if the cell to the right of the current cell is unoccupied,
        #fill in the cell w/ the character
        if currentBoard[row-1][col] != (" ") and currentBoard[row][col+1] == (" "):
            currentBoard[row][col+1] = character
            if userAns == "yes":
                printBoard(currentBoard)
            autoFill(userAns,character,currentBoard,row,col+1)
        
        #if the cell below the current cell is unoccupied,
        #fill in the cell w/ the character 
        if currentBoard[row-1][col] != (" ") and currentBoard[row][col+1] != (" ") and currentBoard[row+1][col] == (" "):
            currentBoard[row+1][col] = character
            if userAns == "yes":
                printBoard(currentBoard)
            autoFill(userAns,character,currentBoard,row+1,col)
        
        #if the cell to the left of the current cell is unoccupied,
        #fill in the cell w/ the character
        if currentBoard[row-1][col] != (" ") and currentBoard[row][col+1] != (" ") and currentBoard[row+1][col] != (" ") and currentBoard[row][col-1] == (" "):
            currentBoard[row][col-1] = character
            if userAns == "yes":
                printBoard(currentBoard)
            autoFill(userAns,character,currentBoard,row,col-1)
     
def main():
    
    userInput = ""
    rows = 0
    columns = 0
    userBoard = []
    
    #asking user for name of a file
    fileName = input("Please enter a file for input: ")
    #file must end with .dat or .txt
    while fileName[-4:] != ".dat" and fileName[-4:] != ".txt":
        fileName = input("That is not a valid filename -- please enter a filename\n\tthat ends in \".dat\" or \".txt\": ")
        
    #open file for reading
    userFile = open(fileName, 'r')

    #read in and store the board in a 2D list
    for line in userFile:
        line = line.strip()
        characterList = []
        for character in line:
            characterList.append(character)
        userBoard.append(characterList)
    
    #count the number of rows in the 2D list
    for row in userBoard:
        rows = rows + 1
    
    #count the number of columns in the 2D list, using the first row 
    for col in range(len(userBoard[0])):
        columns = columns + 1

    while userInput != "Q":
        
        printBoard(userBoard)

        userInput = input("\nPlease enter the coordinates you would like to start\nfilling at in the form \"row,col\", or Q to quit: ")
        
        if userInput != "Q":
            row,col = checkInput(userInput,rows,columns)
        
            symbol = input("Please enter a symbol to fill with: ")
            #reprompt user if the symbol isnt a single character
            while len(symbol) != 1:
                print("The symbol \"",symbol,"\" is not a single character.")
                symbol = input("Please enter a symbol to fill with: ")

            #if the coordinate given by user is unoccupied, fill w/ the symbol
            if userBoard[row][col] == (" "):
                userBoard[row][col] = symbol

            print("Would you like to show each step of the recursion? ")
            userAns = input("Enter \"yes\" or \"no\": ")
            #reprompt user if the answer is not "yes" or "no"
            while userAns != "yes" and userAns != "no":
                print("The choice \"",userAns,"\" is not valid.")
                print("Would you like to show each step of the recursion? ")
                userAns = input("Enter \"yes\" or \"no\": ")
            
            if userAns == "yes":
                printBoard(userBoard)
                autoFill(userAns,symbol,userBoard,row,col)
            print("---------------------------------\n")

    userFile.close()
    print("Thank you for using the autofill program!")

main()
