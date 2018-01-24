def main():
    
    scores = []
    total = 0
    avg = 0
    userInput = ""
    while userInput != "exit":
        userInput = input("Please enter a score (0 to 10) or exit to stop: ")
        if userInput != "exit":
            scores.append(int(userInput))
    for n in scores:
        total += n
    print("Total:",total)
main()
