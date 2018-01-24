#File: testLab12.py

def wordDic(dicFile):
    
    tranDict = {}
    words = []
    
    for line in dicFile:
        line = line.split()
        

def main():
    
    engWord = ""
    
    wordFile = open("eng2sp.txt",'r')
    dictionary = wordDic(wordFile)
    
    while engWord != 'Exit':
        engWord = input("Please enter the English word you would like to translate.\n(Enter the word 'EXIT' to quit the program): ")

    print("Thank you for using the English -> Spanish translator!")
main()
