#File:        hw4_part5.py
#Author:      Marinna Ricketts-Uy
#Date:        9/30/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program counts the number of times a character appears in
#             a string.

def main():
    #prompt user for input
    string = input("Please enter a string: ")
    char = input("Please enter a character: ")
    
    #intialize variable
    totalChar = 0
    #for each character in the string
    for c in string:
        #if given character appears in the string,keep totaling each instance
        #in the variable totalChar
        if char.lower() == c or char.upper() == c:
            totalChar = totalChar + 1
    print("The character \'" + char + "\' appears ",totalChar, " times in the string: \n\t\'" + string + "\'.")
main()
