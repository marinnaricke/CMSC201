#Description: PRACTICE FOR LAB 7 

def main():
    
    #initializing two lists
    items = ["shoes","socks", "hat", "belt", "blouse", "dress", "tie"]
    prices = [ 54.99, 7.11, 6.49, 22.58, 21.73, 38.99, 14.83]
    #user starts with $100 in their wallet
    userFunds = float(100)
    #initialized variable for user input
    userInput = 1
    
    while userInput != 0:
        print("You have $",userFunds,"in funds available")
        #looping over the length of the items list
        for i in range(len(items)):
            #numbering will start at 1
            print(i+1,"-",items[i],"\t","$",prices[i])
        userInput = int(input("Please choose an item # to purchase, or '0' to quit: "))
        if userFunds >= prices[userInput-1] and userInput != 0:
            print("\nThank you for purchasing:",items[userInput-1],"\n")
            userFunds = userFunds - prices[userInput-1]
        elif userFunds < prices[userInput-1]:
            print("Sorry, but you are unable to afford that item. \n")
    print("\nThank you for shopping at Python Mart!\nYou have","$",userFunds,"left in your wallet.\nHave a great day!")
main()
