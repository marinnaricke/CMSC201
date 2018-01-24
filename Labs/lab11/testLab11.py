#Test Lab11

class Ong:
    def __init__(self,word):
        self.word = word
    def isVowel(self,letter):
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "o" or letter.lower() == "u":
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
            print(newLetter,end = "")
        print()

def main():
    userString = Ong(input("Enter a string to translate: "))
    userString.translateOng()

main()
