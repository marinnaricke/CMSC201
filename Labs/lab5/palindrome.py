#File:        palindrome.py
#Author:      Marinnna Ricketts-Uy
#Date:        10/1/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program takes in a string from the user and checks if it
#             is a palindrome.

def main():

    string = input("Please enter a string: ")
    string2 = []
    #for c in string:
    string2 = (string[::-1])
    print(string2)
    if string == string2:
        print(string + " is a palindrome.")
    else:
        print(string + " is not a palindrome.")
main()
