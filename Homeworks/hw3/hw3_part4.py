#File:        hw3_part4.py
#Author:      Marinna Ricketts-Uy
#Date:        9/17/15
#Lab Section: 17
#Umbc Email:  pd12778@umbc.edu
#Description: This program asks the user about the state of two switches and
#             uses that information to determine the state of a generator.

def main():

    print("Please enter 'y' for yes and 'n' for no.")
    
    isFirstSwitch = input("\nIs the first switch on? (y/n): ")
    isSecondSwitch = input("Is the second switch on? (y/n): ")
    if (isFirstSwitch == "y" and isSecondSwitch == "y") or \
            (isFirstSwitch == "n" and isSecondSwitch == "n"):
        print("\nThe generator is off.")
    else:
        print("\nThe generator is on.")
main()
