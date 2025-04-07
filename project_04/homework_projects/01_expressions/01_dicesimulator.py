# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.


import random  

def roll_dice():
    print("Rolling two dice three times...")  

    for roll in range(3):  
        die1 = random.randint(1, 6)  
        die2 = random.randint(1, 6)  
        print(f"Roll {roll + 1}: Die 1 = {die1}, Die 2 = {die2}")  

roll_dice() 


