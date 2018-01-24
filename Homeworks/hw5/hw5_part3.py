#File:        hw5_part3.py
#Author:      Marinna Ricketts-Uy
#Date:        10/13/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program stimulates the up and down movement of a hailstone
#             in a storm. It asks the user for a positive integer that will be
#             the starting height of the hailstone.

def main():
    #prompts user for input
    hailHeight = int(input("Please input the starting height of the hailstone: "))
    print("Hail is currently at height",hailHeight)
    #enters the loop until hailHeight is equal to 1
    while hailHeight != 1:
        #if even, divide by 2. if not, multiply by 3 and then add 1
        if hailHeight % 2 == 0:
            hailHeight = hailHeight // 2
            print("Hail is currently at height", hailHeight)
        else:
            hailHeight = hailHeight * 3 + 1
            print("Hail is currently at height", hailHeight)
main()
