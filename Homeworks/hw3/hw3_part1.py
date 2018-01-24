#File:        hw3_part1.py
#Author:      Marinna Ricketts-Uy
#Date:        9/17/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: Reading in three floats from the user and printing the average.

def main():
    
    num1 = float(input("Please enter a floating point number: "))
    num2 = float(input("Please enter a second floating point number: "))
    num3 = float( input("Please enter a third floating point number: "))
   
    average = (num1 + num2 + num3)/ 3
    print("\nThe average of the three floats is: ",average)
main()
