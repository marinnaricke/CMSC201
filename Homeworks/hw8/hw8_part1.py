#File:        hw8_part1.py
#Author:      Marinna Ricketts-Uy
#Date:        11/24/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program takes in a list of integers and prints out
#             the reverse of that list using recursion

#rev() Prints out the reverse of a list
#input: the list of integers provided by user
#output: Reverse of that list
def rev(numList, i):
    print(numList[i])
    #if the list item is not eqaul to the first item in the list,
    #keep decreasing i 
    if numList[i] != numList[0]:
        rev(numList,i-1)
    
def main():
    i = -1
    numList = []
    userInput = 0
    
    while userInput != -1:
        userInput = int(input("Enter a number to append to the list, or -1 to stop: "))
        if userInput != -1:
            numList.append(userInput)
    
    print("The list as you entered it is: ", numList)
    print("The reversed list is: ")
    
    rev(numList, i)

main()
