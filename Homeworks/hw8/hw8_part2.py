#File:        hw8_part2.py
#Author:      Marinna Ricketts-Uy
#Date:        11/24/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program asks the user for input in order to
#             print a right triangle using recursion

# tri() Creates a right triangle made out of a character
# Input: height of the triangle and character that the triangle is made of
# Output: the right triangle 
def tri(intHeight,character):
    print(character * intHeight)
    #if height is not equal to 1, keep decreasing the height
    if (intHeight > 1):
        tri(intHeight - 1,character)

def main():
    height = int(input("Please enter the height of your triangle: "))
    
    while height <= 0:
        print("Your triangle height must be positive (> 0). ")
        height = int(input("Please enter the height of your triangle: "))
    
    symbol = input("Please enter a character for your triangle: ")
    print()
    
    tri(height,symbol)

main()
