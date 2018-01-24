#File:        temperature.py
#Author:      Marinna Ricketts-Uy
#Date:        9/24/15
#Section:     17
#E-mail:      pd12778@umbc.edu
#Description: This program asks the user to enter the temperature in Farenheit
#             and the program prints out a description of the weather 

def main():

    temp = int(input("Please enter a temperature in Farenheit: "))
    if temp < 25:
        print("It's freezing outside.")
    elif temp >= 25 and  temp <= 49:
        print("It's a bit chilly, remember to bundle up.")
    elif temp >= 50 and temp <= 79:
        print("The weather is wonderful!")
    elif temp >= 80 and temp <= 100:
        print("It's pretty hot outside.")
    else:
        print("It is way too hot.")
main()
