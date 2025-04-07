import random

def get_user_choice():
    """Get and validate user input."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_choice = input("\nChoose: (R)ock, (P)aper, (S)cissors or (Q)uit: ").lower()
        if user_choice in choices:
            return user_choice, choices[user_choice]
        elif user_choice == 'q':
            return 'q', 'Quit'
        print("⚠️ Invalid choice! Please select R, P, or S.")

def determine_winner(user, computer):
    """Determine the winner based on game rules."""
    rules = {'r': 's', 's': 'p', 'p': 'r'}
    if user == computer:
        return "🤝 It's a tie!"
    elif rules[user] == computer:
        return "🎉 You win!"
    else:
        return "💀 You lose!"

def play_game():
    """Play multiple rounds of Rock-Paper-Scissors."""
    print("\n🕹️ Welcome to Rock-Paper-Scissors!")
    
    user_score, computer_score = 0, 0

    while True:
        user, user_name = get_user_choice()
        if user == 'q':
            break

        computer = random.choice(['r', 'p', 's'])
        choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
        print(f"\n🧑 You chose: {user_name}  |  🤖 Computer chose: {choices[computer]}")

        result = determine_winner(user, computer)
        print(result)

        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"📊 Score: You [{user_score}] - Computer [{computer_score}]")

    print("\n👋 Thanks for playing! Final Score: You [{}] - Computer [{}]".format(user_score, computer_score))
    if user_score > computer_score:
        print("🏆 Congratulations! You won the game overall! 🎉")
    elif user_score < computer_score:
        print("🤖 The computer wins overall! Better luck next time! 💀")
    else:
        print("🤝 It's a tie overall! Well played! 🎯")


play_game()
