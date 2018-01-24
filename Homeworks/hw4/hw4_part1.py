#File:        hw4_part1.py
#Author:      Marinna Ricketts-Uy
#Date:        9/29/15
#Lab Section: 17
#UMBC email:  pd12778@umbc.edu
#Description: This program is written to draw a right triangle.

def main():
    #prompt user for input
    height = int(input("Please enter the height of your triangle: "))
    symbol = input("Please enter a single character for the symbol: ")
    #run the loop up to given height
    for n in range(height):
        n = n + 1
        print(symbol*n)
main()
