# File:        hw2.py
# Written by:  Marinna Ricketts-Uy
# Date:        9/10/15
# Lab Section: 17
# Umbc Email:  pd12778@umbc.edu
# Description: This program is for practicing order of operations and modulo in
#              a Python environment.


def main():

    print("Marinna Ricketts-Uy")
    print("Description: Practice with order of operations and modulo ")
    print("Instructions: Simply run the program")

    # Question 1: 
    # Expected output: 24
    num1 = (7 + 1) * 3
    print("Question 1 evaluates to:", num1)
    # Actual output: 24
    # Explanation: Parentheses evaluated first (8), then multiplication (24).
    
    # Question 2:
    # Expected output: 2
    num2 = (12 % 5)
    print("Question 2 evaluates to:",num2)
    # Actual output: 2
    # Explanation: 12 divided by 5 equals 2 with a remainder of 2.
    #              So (12 % 5) equals the remainder of 2.
    
    # Question 3:
    # Expected output: 21
    num3 = (21 % 49)
    print("Question 3 evaluates to:",num3)
    # Actual output: 21
    # Explanation: The remainder equals 21.

    # Question 4:
    # Expected output: 2
    num4 = (5-3) + (10-5) * (8%2)
    print("Question 4 evaluates to: ",num4)
    # Actual output: 2
    # Explanation: Evaluate the numbers in the parentheses first. (2)+(5)*(0)
    #              Then multiplication (0) and finally addition (2).
    
    # Question 5:
    # Expected output: 34
    num5 = 6.5 + 5 / 2 * (4 + 7)
    print("Question 5 evaluates to: ",num5)
    # Actual output: 34.0
    # Explanation: Parentheses first (11), then division (2.5) and
    #               multiplication (27.5), then addition (34.0). 
    #               My mistake was 6.5 + 27.5 = 34.0, and I thought it was 34.

    # Question 6:
    # Expected output: 5
    num6 = 9 / 3 + 18 - 4 * 4
    print("Question 6 evaluates to: ",num6)
    # Actual output: 5.0
    # Explanation: Division first (3.0) and multiplication (16), then
    #              addition (21) and then subtraction (5).
    #              My mistake was 9 / 3 = 3.0, and I thought it was 3.

    # Question 7:
    # Expected output: 22
    num7 = 8 % 3 + 5 * 4
    print("Question 7 evaluates to: ",num7)
    # Actual output: 22
    # Explanation: Modulo (2) and multiplication (20), then addition (22).

    # Question 8:
    # Expected output: 79.91428571428571
    num8 = 81.3 / 2.1 + ((51.5 % 65.2) * 2 / 2.5)
    print("Question 8 evaluates to: ",num8)
    # Actual output: 79.91428571428571
    # Explanation: Parentheses first which then includes  modulo (51.5) and
    #              multiplication (103) and division (41.2).
    #              Then division (38.71428571428571).
    #              Then addition (79.91428571428571).

    # Question 9:
    # Given equation: 100 - 8 * 8 + 1 / 0.5
    # Solved equation: 
    # Target: -30
    num9 = 100 - ((8 * 8) + 1) / 0.5
    target9 = -30
    print("Question 11 evaluates to: ", num9, "and should be", target9)

    # Question 10:
    # Given equation: 84 / 10 + 11 - 4 * 4
    # Solved equation: ((84 / (10 + 11) - 4) * 4
    # Target: 0
    num10 = ((84 / (10 + 11) - 4)) * 4
    target10 = 0
    print("Question 10 evaluates to: ",num10, "and should be",target10)

main()
