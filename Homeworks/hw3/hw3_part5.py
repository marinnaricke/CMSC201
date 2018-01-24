#File:        hw3_part5.py
#Author:      Marinna Ricketts-Uy
#Date:        9/17/15
#Lab Section: 17
#Umbc Email:  pd12778@umbc.edu
#Description: This program is a simplified day of the week calculator.
#             The program asks the user for a day of the month and based upon
#             the number, a day of the week is printed.

def main():

    numDay = int(input("Please enter the day of the month: "))
    if numDay < 1 or numDay > 31:
        print("Invalid day!")
    elif numDay == 1 or numDay == 8 or numDay == 15 or numDay == 22 \
            or numDay == 29:
        print("Today is a Monday!")
    elif numDay == 2 or numDay == 9 or numDay == 16 or numDay == 23 \
            or numDay == 30:
        print("Today is a Tuesday!")
    elif numDay == 3 or numDay == 10 or numDay == 17 or numDay == 24 \
            or numDay == 31:
        print("Today is a Wednesday!")
    elif numDay == 4 or numDay == 11 or numDay == 18 or numDay == 25:
        print("Today is a Thursday!")
    elif numDay == 5 or numDay == 12 or numDay == 19 or numDay == 26:
        print("Today is a Friday!")
    elif numDay == 6 or numDay == 13 or numDay == 20 or numDay == 27:
        print("Today is a Saturday!")
    elif numDay == 7 or numDay == 14 or numDay == 21 or numDay == 28:
        print("Today is a Sunday!")
main()
