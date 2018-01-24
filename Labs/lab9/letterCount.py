#File: letterCount.py
#Author: Marinna Ricketts-Uy
#Date: 10/29/15
#Lab Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: Debugging this code. All errors are in the letterCount function

#letterCount should take a letter and word,
#and count the number of times letter appears
#in the word
def letterCount(letter,myString):
    count = 0
    for i in myString:
        if i == letter:
            count += 1
    print(count)

#no errors below this line
def main():
    print("Should print: 3\nPrints: ", end="")
    letterCount("a","aardvark")
main()
