#File:      calculateMPG.py
#Author:    Marinna Ricketts-Uy
#Date:      9/17/15
#Section:   17
#E-mail:    pd12778@umbc.edu
#Description:  Simple program for calculating mpg

def main():

    milesDriven = int(input("Please enter the distance traveled (in miles):"))
    gallons = int(input("Please enter the gallons used:" ))
    mpg = milesDriven/gallons
    print("The MPG is:",mpg)
main()
