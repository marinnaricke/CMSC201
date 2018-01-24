#File:        hw7.py
#Author:      Marinna Ricketts-Uy
#Date:        10/26/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program uses functions in order to get a list of integers
#             and then find statistics of the given list of integers.

# getList() gets a list of integers from the user
# Output: prompts the user for integers and returns the list
def getList():
    #initializes the list to an empty list 
    intList = []
    userInput = ""
    print("Enter a list of integers or 'q' to end the list!")
    #keeps asking the user for an integer until 'q' is entered
    while userInput != 'q':
        userInput = input("Enter an integer: ")
        #adds the user input to the list except 'q'
        if userInput != 'q':
            userInput = int(userInput)
            intList.append(userInput)
    return intList

# printMenu() Prints a menu of options to the screen
# Output: asks the user for a number and returns the number 
def printMenu():
    print("Please choose the statistic you would like to calculate!")
    print("1. Min\n" + "2. Max\n" + "3. Mean\n" + "4. Median\n" + "5. Clear List")
    userChoice = int(input("Please enter your choice, or 0 to exit: "))
    return userChoice

# getMin() Finds the lowest value in the list created by the user
# Input: the user's list
# Output: the minimum value
def getMin(userList):
    minValue = userList[0]
    #for loop to find the lowest value in the set
    for i in range(len(userList)):
        if userList[i] < minValue:
            minValue = userList[i]
    print("The minimum value is:",minValue)

# getMax() Finds the highest value in the list created by the user
# Input: the user's list
# Output: the maximum value
def getMax(userList):
    maxValue = userList[0]
    #for loop to find the highest value in the set
    for i in range(len(userList)):
        if userList[i] > maxValue:
            maxValue = userList[i]
    print("The maximum value is:",maxValue)

# getMean() Calculates the average value in the list created by the user
# Input: the user's list
# Output: the mean value
def getMean(userList):
    total = 0
    #for loop to calculate the average value in the set
    for i in userList:
        total = total + i
    meanValue = total/len(userList)
    print("The mean value is:",meanValue)

# getMedian() Finds the median value in the list created by the user
# Input: the user's list
# Output: the median value
def getMedian(userList):
    #for loop to find the median value in the set
    for i in userList:
        #sorts the list from least to greatest
        userList.sort()
    #calculates the median if the length of the list is even
    if (len(userList) % 2) == 0:
        num = len(userList) // 2
        total = userList[num - 1] + userList[0 - num]
        medianValue = total / 2
        print("The median value is: ",medianValue)
    #calculates the median if the length is odd
    else:
        num = len(userList) - 1
        medianValue = userList[num // 2]
        print("The median value is:",medianValue)

# emptyList() Empties the current list/calls getList() to repopulate the list
# Input: the user's list
# Output: returns the repopulated list
def emptyList(userList):
    userList = []
    userList = getList()
    return userList

def main():
    print("Welcome to the List Statistics Calculator")
    numList = getList()
    choice = printMenu()
    #keeps printing the menu unless the user chooses 0
    while choice != 0:
        if choice == 1:
            getMin(numList)
            choice = printMenu()
        elif choice == 2:
            getMax(numList)
            choice = printMenu()
        elif choice == 3:
            getMean(numList)
            choice = printMenu()
        elif choice == 4:
            getMedian(numList)
            choice = printMenu()
        elif choice == 5:
            numList = emptyList(numList)
            choice = printMenu()
    print("Thank you for using our calculator")
main()
