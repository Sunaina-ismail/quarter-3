import random

def computer_guess_game():
    print("\n🤖 Welcome to the Guess the Number Game!")


    while True:
        try:
            limit = int(input("Enter the maximum number for the guessing range: "))
            if limit < 1:
                print("⚠️ Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

    low, high = 1, limit
    response = ""
    attempts = 0 

    print(f"\n🔎 Think of a number between 1 and {limit} and let the computer guess it!")

    while response != "c":
        attempts += 1  

    
        if low > high:
            print("⚠️ Error! Your responses have led to an impossible situation. Restarting game.")
            return  

        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  

        response = input(f"Is {computer_guess} too high (H), too low (L), or correct (C)? ").lower()

       
        while response not in ["h", "l", "c"]:
            response = input("⚠️ Invalid input! Please enter 'H' for too high, 'L' for too low, or 'C' for correct: ").lower()

        if response == "h":
            if computer_guess == low:
                print("⚠️ That doesn't make sense! You said it was too high, but it's the lowest possible number.")
                continue
            high = computer_guess - 1
        elif response == "l":
            if computer_guess == high:
                print("⚠️ That doesn't make sense! You said it was too low, but it's the highest possible number.")
                continue
            low = computer_guess + 1

    print(f"\n🎯 Boom! The computer guessed your number: {computer_guess} in {attempts} attempts.")


computer_guess_game()
