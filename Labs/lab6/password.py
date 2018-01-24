#File:        password.py
#Author:      Marinna Ricketts-Uy
#Date:        10/8/15
#Section:     17
#E-mail:      pd12778@umbc.edu
#Description: This program takes in a password guess from the user and checks if
#             their guess matches the actual password. The user gets three 
#             chances to enter the correct password.

def main():
    userGuess = str(input("Enter the password: "))
    password = "UMBCrulz"
    numCount = 3
    while numCount > 1:
        numCount = numCount - 1
        if userGuess == password:
            print("User guess was accepted.")
            numCount = 0
        else:
            print("The guess was incorrect. You have ",numCount," guesses left")
            userGuess = str(input("Enter the password: "))
        if numCount == 1:
            print("You cannot access the system.")
main()
