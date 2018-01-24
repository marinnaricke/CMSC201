#File: store.py
#Author: Marinna Ricketts-Uy
#Date: 10/15/15
#Section: 17
#UMBC Email: pd12778@umbc.edu
#Description: This program lets a user "shop" in the store by choosing items
#             to purchase and being "charged" for those items.

def main():
    
    items = ["shoes","socks","hat","belt","blouse","dress","tie"]
    prices = [54.99,7.11,6.49,22.58,21.73,38.99,14.83]
    for i in range(len(items)):
        print(i+1,"-",items[i],"\t","$",prices[i]) 
main()
