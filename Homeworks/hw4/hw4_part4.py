#File:        hw4_part4.py
#Author:      Marinna Ricketts-Uy
#Date:        9/30/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program outputs the numbers from 1 to 100 (inclusive), one
#             per line. However, there are three special cases where instead of 
#             printing the number, you print a message instead.

def main():
    #this is rearranged from what was turned in. I just flipped the third elif and the first if. 
    #run loop up to 100
    for n in range(1,101):
        #if divisible by 3 and 5
        if (n % 3) == 0 and (n % 5) == 0:
            print("In the future,everyone will be world-famous for 15 minutes.") 
        #if divisible by 5
        elif (n % 5) == 0:
            print("Where do you see yourself in five years?")
        #if divisible by 3
        elif (n % 3) == 0:
            print("Better three hours too soon than a minute too late.")
        else:
            print(n)
main()
