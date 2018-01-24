#File: factorial.py
#Author: Marinna Ricketts-Uy
#Date: 10/29/15
#Lab Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: Find the errors in the snippet of code

#factorial(n) computes the factorial of a number n
#the factorial of a number n is defined as:
# factorial(n) = n * (n-1) * (n-2) * ... * 2 * 1
def factorial(n):
    product = n
    for X in range(1,n):
        product = product * (n-X)
    return product

#no errors below this line
def main():
    print("Should print: 120\nPrint: ",end="")
    print(factorial(5))
main()
