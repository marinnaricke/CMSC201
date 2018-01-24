#File:        hw8_part3.py
#Author:      Marinna Ricketts-Uy
#Date:        11/24/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program uses a recursive function to find the greatest
#             common denominator of two integers.

# gcd() Finds the greatest common denominator of two integers
# Input: the two integers from the user input and a integer called remainder
# Output: the greatest common denominator
def gcd(num1,num2,remainder):
    #take the mod of the two integers to find the remainder
    remainder = num1 % num2
    #set the first integer equal to the second integer
    num1 = num2
    #set the second integer equal to the remainder
    num2 = remainder

    #if the second integer(also the remainder) equal to 0,
    #return the first integer, which is then equal to the gcd
    if num2 == 0:
        return num1
    else:
        return gcd(num1,num2,remainder)

def main():
    remainder = 0
    firstInt = int(input("Please enter the first integer: "))
    
    while firstInt <= 0:
        print("Your number must be positive (greater than 0). ")
        firstInt = int(input("Please enter the first integer: "))
    
    secondInt = int(input("Please enter the second integer: "))
    
    while secondInt <= 0:
        print("Your number must be positive (greater than 0). ")
        secondInt = int(input("Please enter the second integer: "))
    
    print("The GCD of",firstInt,"and",secondInt,"is",gcd(firstInt,secondInt,remainder))
    print()

main()
