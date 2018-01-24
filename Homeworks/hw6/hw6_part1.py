#File:        hw6_part1.py
#Author:      Marinna Ricketts-Uy
#Date:        10/17/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program creates a simple text file, called names.txt based
#             on input from the user.

def main():
    #initialize variable called userInput to store the input from the user
    userInput = ""
    #continues writing to the file until the user types 'DONE'
    while userInput != "DONE":
        userInput = input("Please enter a name (or 'DONE' to stop): ")
        #writes the users input to the file except the word 'DONE'
        if userInput != "DONE":
            nameFile = open("names.txt", "a")
            nameFile.write("Hello " + userInput + "! \n")
    nameFile.close()
main()
