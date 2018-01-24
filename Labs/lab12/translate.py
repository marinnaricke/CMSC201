#File:        translate.py
#Author:      Marinna Ricketts-Uy
#Date:        12/3/15
#Section:     17
#UMBC Email:  pd12778@umbc.edu
#Description: This program implements a very simple English to Spanish translator using a dictionary.

def wordDic(dicFile):
    
    tranDict = {}
    
    for line in dicFile:
        line = line.strip()
        (key,val) = line.split()
        tranDict[key] = val
        
    return tranDict

def main():
    
    engWord = ""
    
    wordFile = open("eng2sp.txt",'r')
    dictionary = wordDic(wordFile)
    
    while engWord != 'EXIT':
        engWord = input("\nPlease enter the English word you would like to translate.\n(Enter the word 'EXIT' to quit the program): ")
        if engWord != 'EXIT':
            if engWord in dictionary:
                print("\n\tIn Spanish, the word \"" + engWord + "\" is \"" + dictionary[engWord] + "\"")
            else:
                print("\n\tSorry, I do not know the word \"" + engWord + "\"")

    print("\nThank you for using the English -> Spanish translator!")
main()
