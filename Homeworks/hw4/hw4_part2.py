#File:        hw4_part2.py
#Author:      Marinna Ricketts-Uy
#Date:        9/29/15
#Lab Section: 17
#UMBC email:  pd12778@umbc.edu
#Description: This program asks the user for input in order to draw an 
#             empty box.

def main():
    #prompt user for three inputs
    width = int(input("Please enter the width for the box: "))
    height = int(input("Please enter the height for the box: "))
    symbol = input("Please enter a single character for the symbol: ")
    
    #first line to be printed
    print(symbol*width)
    #this will allow the box not to be filled in
    for n in range(height-2):
        n = n - 1
        space = width - 2
        print(symbol + " "*space + symbol)
    #if height is larger than 1,print a bottom line
    if height > 1:
        print(symbol*width)
main() 
