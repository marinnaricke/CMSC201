#File:        hw6_part3.py
#Author:      Marinna Ricketts-Uy
#Date:        10/17/15
#Lab Section: 17
#UMBC Email:  pd12778@umbc.edu
#Description: This program takes in the name of a file from the user and 
#             calculates the total number of words in the file, as well as the 
#             average word length.

def main():
    #initialize variables
    totalWords = 0
    totalChar = 0
    fileName = input("Please enter the name of the file to open: ")
    #will keep re-prompting the user until a valid filename is choosen
    #for this program, the filename must end in .txt or .dat
    while fileName[-4:] != ".txt" and fileName[-4:] != ".dat":
         print("The file must end in .txt or .dat to be vaild.")
         fileName = input("Please enter the name of the file to open: ")
    userFile = open(fileName, 'r')
    #reads through each line in the file
    for line in userFile:
        words = line.split()
        #counts how many words are on each line
        for word in words:
            totalWords = totalWords + 1
            #counts how many characters are in each word
            for c in range(len(word)):
                totalChar = totalChar + 1
    avg = totalChar/totalWords
    userFile.close()
    print("The file",fileName,"has",totalWords,"words in it.")
    print("On average, each word is",avg,"characters long.")
main()
