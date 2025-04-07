import random

def user_guess_game(limit):
    secret_number = random.randint(1, limit)
    guess = None  

    print("\n🔢 Let's play! Try to guess the secret number.")

    while guess != secret_number:
        try:
            guess = int(input(f"Enter a number between 1 and {limit}: "))
            if guess < secret_number:
                print("📉 Too low! Give it another shot.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
        except ValueError:
            print("⚠️ Oops! Please enter a valid number.")

    print(f"🎉 Woohoo! You nailed it! The secret number was {secret_number}.")

def computer_guess_game(limit):
    low, high = 1, limit
    response = ""

    print("\n🤖 Now it's my turn to guess!")

    while response != "c":
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  

        response = input(f"Is {computer_guess} too high (H), too low (L), or correct (C)? ").lower()

        if response == "h":
            high = computer_guess - 1
        elif response == "l":
            low = computer_guess + 1

    print(f"🎯 Boom! I guessed it right! Your number was {computer_guess}.")


user_guess_game(20)
