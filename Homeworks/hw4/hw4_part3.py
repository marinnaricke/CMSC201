#File:        hw4_part3.py
#Author:      Marinna Ricketts-Uy
#Date:        9/30/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program asks the user for input to determine whether a 
#             subject can be studied or not.

def main():
    #initialize variable
    size = 10
    subjects_list = [None]*size

    for n in range(size):
        subjects_list[n] = input("Please enter a subject: ")
    for s in subjects_list:
        #check each string in the list
        #if the string ends in 'ology',print 'You can study' followed by string
        #if not, print the string
        if s[-5:] == 'ology' :
            print("You can study " + s)
        else:
            print(s)
main() 
