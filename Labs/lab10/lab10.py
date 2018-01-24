#File: lab10.py
#Author: Marinna Ricketts-Uy
#Date: 11/5/15
#Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: Creating a Caesar Cipher

def main():
    print("What would you like to do?\n1. Encrypt String\n2. Decrypt String")
    choice = int(input("Enter 1 or 2: "))
    
    if choice == 1:
        shift = int(input("How much would you like to shift? (1-26): "))
        encrypt(shift)
    elif choice == 2:
        shift = int(input("How much would you like to shift? (1-26): "))
        decrypt(shift)

def encrypt(n):
    newString = []
    string = input("Enter plain text message: ")
    for i in string:
        newChar = ord(i) + n
        if newChar > ord("Z"):
            newChar = newChar - 26
        newChar = chr(newChar)
        newString.append(newChar)
    print("Your encrypted message is: ")
    for i in newString:
        print(i,end="")
    print()

def decrypt(n):
    newString = []
    string = input("Enter encrypted message: ")
    for i in string:
        newChar = ord(i) - n
        if newChar < ord("A"):
            newChar = newChar + 26
        newChar = chr(newChar)
        newString.append(newChar)
    print("Your plain text message is: ")
    for i in newString:
        print(i,end="")
    print()

main()
