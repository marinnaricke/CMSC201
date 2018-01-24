#File:        hw3_part3.py
#Author:      Marinna Ricketts-Uy
#Date:        9/17/15
#Lab Section: 17
#Umbc Email:  pd12778@umbc.edu
#Description: This program is used to create a medical diagnosis by
#             prompting the user for yes or no answers.

def main():

    print("Enter 'y' for yes and 'n' for no to the following questions.")
    
    hasFever = input("\nDo you have a fever? (y/n): ")
    if hasFever == "n":
        hasStuffy = input("Do you have a stuffy nose? (y/n): ")
        if hasStuffy == "n":
            print("\nYour diagnosis: You are a Hypochondriac.")
        else:
            print("\nYour diagnosis: You have a Head Cold.")
    elif hasFever == "y":
        hasRash = input("Do you have a rash? (y/n): ")
        if hasRash == "n":
            isEarHurt = input("Does your ear hurt? (y/n): ")
            if isEarHurt == "n":
                print("\nYour diagnosis: You have the Flu.")
            else:
                print("\nYour diagnosis: You have an Ear Infection.")
        else:
            print("\nYour diagnosis: You have the Measles.")

main()
