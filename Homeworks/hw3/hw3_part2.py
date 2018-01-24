#File:        hw3_part2.py
#Author:      Marinna Ricketts-Uy
#Date:        9/17/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: Program that propmts user for input in order to calculate grades.

def main():

    weightHw = float(input("Please enter the homework weight: "))
    gradeHw = float(input("Please enter the homework grade: "))

    weightEx = float(input("Please enter the exam weight: "))
    gradeEx = float(input("Please enter the exam grade: "))

    weightDi = float(input("Please enter the discussion weight: "))
    gradeDi = float(input("Please enter the discussion grade: "))

    total = (weightHw * gradeHw) + (weightEx * gradeEx) + (weightDi * gradeDi)
    if total >= 90:
        print("\nThe final numerical grade is: ",total)
        print("This earns you an A in the class.")
    elif total <= 89.9:
        print("\nThe final numerical grade is: ",total)
        print("This earns you a B in the class.")
    elif total <= 79.9:
        print("\nThe final numerical grade is: ",total)
        print("This earns you a C in the class.")
    elif total <= 69.9:
        print("\nThe final numerical grade is: ",total)
        print("This earns you a D in the class.")
    elif total <= 59.9:
        print("\nThe final numerical grade is: ", total)
        print("This earns you an F and you have failed the course.")
main()
