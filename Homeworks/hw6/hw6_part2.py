#File:        hw6_part2.py
#Author:      Marinna Ricketts-Uy
#Date:        10/17/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program calculates a weighted grade from data contained in
#             a file. The file choosen by the user input

def main():
    #initialize variables 
    weightedTotal = 0
    fileName = input("Please enter the name of the file: ")
    #opens file for reading
    userFile = open(fileName, 'r')
    #reads each line in the given file
    for line in userFile:
        fileContents = line.split()
        #sets the first item in the line to a variable called weight
        weight = fileContents[0]
        #sets the remaining items in the line to a list called grades
        grades = fileContents[1:]
        total = 0
        #a loop for each grade
        for g in grades:
            total = total + int(g)
        avg = total/len(grades)
        weightedTotal = weightedTotal + (avg*float(weight))
    userFile.close()
    print("Your final weighted score is",weightedTotal)
main()
