def isPalindrome(myString):
    tempString = myString
    length = len(tempString)
    half = length/2
    isPalindrome = True
    for i in range(int(half)):
        if tempString[i] != tempString[length-i-1]:
            isPalindrome = False
    print(isPalindrome)

#no errors below this line
def main():
    print("Should print: True\nPrints: ",end="")
    isPalindrome("tacocat")
    print("Should print: False\nPrints: ",end="")
    isPalindrome("pineapple")
main()
