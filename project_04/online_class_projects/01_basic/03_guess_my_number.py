# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48



import random

def guess_my_number():
    """A simple number guessing game where the user guesses a number between 0 and 99."""
    secret_number = random.randint(0, 99)  
    print("I am thinking of a number between 0 and 99...")

    while True:
            guess = int(input("Enter a guess: "))  
            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
                continue

            if guess > secret_number:
                print("Your guess is too high")
            elif guess < secret_number:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  

guess_my_number()







    
    
