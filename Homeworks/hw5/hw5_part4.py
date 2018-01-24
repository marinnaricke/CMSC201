#File:        hw5_part4.py
#Author:      Marinna Ricketts-Uy
#Date:        10/13/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program takes in two lists of numbers from the user, and creates
#             a pairwise sum.

def main():
    
    userList1 = []
    userList2 = []
    pairWise = []
    num = 0
    listItem1 = ""
    listItem2 = ""
    #while the user doesn't input "end", it will keep prompting the user for integers
    while listItem1 != "end":
        listItem1 = input("Please enter a number (or 'end' to stop): ")
        #as long as the input doesn't equal "end", the input will append to the list 
        if listItem1 != "end":
            userList1.append(int(listItem1))
    print("Thank you for completing the first list.")
    while listItem2 != "end":
        listItem2 = input("Please enter a number (or 'end' to stop): ")
        if listItem2 != "end":
            userList2.append(int(listItem2))
    print("Thank you for completing the second list.")
    #each item in lists are added together, element by element, and
    #appended to a list called pairWise
    for i in range(len(userList1)):
        num = userList1[i] + userList2[i]
        pairWise.append(num)
    print(pairWise)
main()
