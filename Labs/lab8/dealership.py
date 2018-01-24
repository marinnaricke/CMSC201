#File: dealership.py
#Author: Marinna Ricketts-Uy
#Date: 10/22/15
#Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: This program is an example of a used car lot. The program takes
#             in a file called cars.txt and reads the contents. And then based
#             on what a buyer is looking for, goes through that file to find 
#             cars that much the file.

def main():

    carFile = open("cars.txt",'r')
    resultsFile = open("results.txt", 'w')
    for line in carFile:
        carName,carColor,doors,cupHolders,price = line.split(",")
        price = int(price)
        if carColor == "red" and doors == "4" and price < 30000:
            price = str(price)
            resultsFile.write(carName + "---" + "$" + price + "\n")
    carFile.close()
    resultsFile.close()
main()
