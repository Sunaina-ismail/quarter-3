import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")

    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is {user_number}")

 
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either higher or lower: ").lower()

  
    if user_number == computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    elif guess == 'higher' and user_number > computer_number:
        score += 1
        print(f"You were right! The computer's number was {computer_number}")
    elif guess == 'lower' and user_number < computer_number:
        score += 1
        print(f"You were right! The computer's number was {computer_number}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}\n")


print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
