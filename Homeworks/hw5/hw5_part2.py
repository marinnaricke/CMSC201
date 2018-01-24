#File:        hw5_part2.py
#Author:      Marinna Ricketts-Uy
#Date:        10/13/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program prompts the user for a width and height in order to 
#             create a box. 

def main():
    
    width = int(input("Please enter a width: "))
    height = int(input("Please enter a height: "))
    numCount = 0
    #runs the loop until numCount is no longer less than width*height
    #this allows the given height to be met
    while numCount < (width*height):
        #prints a incremented number until the given width is reached  
        for i in range(width):
            numCount = numCount + 1
            print(numCount," ",end="")
        print()
main()
