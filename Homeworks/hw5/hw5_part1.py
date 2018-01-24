#File:        hw5_part1.py
#Author:      Marinna Ricketts-Uy
#Date:        10/13/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program asks the user for a number between 0 and 100
#             (inclusive). A while loop is used to re-prompt the user until
#             they provide a valid number. 

def main():

    #prompt user for input    
    userNum = int(input("Please enter a number (between 0 and 100,inclusive): "))
    #while the number is not between 0 and 100 (inclusive), re-prompt the user
    while userNum < 0 or userNum > 100:
        print("That is an invalid number, please try again." )
        userNum = int(input("Please enter a number (between 0 and 100,inclusive): "))
    print("Thank you for selecting the number",userNum)
main()

