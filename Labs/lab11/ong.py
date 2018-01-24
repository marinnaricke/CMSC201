#File: ong.py
#Author: Marinna Ricketts-Uy
#Date: 11/19/15
#Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: This program takes in a word from the user and turns it into ong language.

class Ong:
    
    def __init__(self,word):
        self.word = word
    def isVowel(self,letter):
        vowelList = ['a','e','i','o','u']
        if letter.lower() in vowelList:
            return True
        else:
            return False
    def translateOng(self):
        newLetter = ""
        for letter in self.word:
            compare = self.isVowel(letter)
            if compare:
                newLetter = letter
            else:
                newLetter = letter + "ong"
            print(newLetter, end="")
        print()
def main():
    userString = Ong(input("Enter a string to translate: "))
    userString.translateOng()
main()
