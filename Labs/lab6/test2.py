def main():
    userInput = input("Please enter your name: ")
    initials = []
    userInput = userInput.split()
    for i in userInput:
        i = i[0]
        initials.append(i.upper())
    for n in initials:
        print(n +".",end="")
    print()
main()
