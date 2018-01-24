#File:    pets.py
#Author:  Marinna Ricketts-Uy
#Date:    9/24/15
#Section: 17
#E-mail:  pd12778@umbc.edu
#Description: This program is to practice comparing strings. First, we will
#             request an input from the user. If the input is "dog" or "cat"
#             exactly, we want to tell the user that it is a pet.

def main():

    animal = input("Please enter the animal you have: ")
    if animal == "dog" or animal == "cat":
        print("This is a pet.")
    else:
        print("This is not a pet.")
main()
