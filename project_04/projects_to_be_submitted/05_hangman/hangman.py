import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    print("🤔 Bored??")
    print("Let's play a game of Hangman! 🎮")
    print("Welcome to Hangman! Get ready to test your word skills! 🎉")
    
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"\n You have {lives} lives left! ")
        print("📜 Letters you've used so far: ", ' '.join(used_letters) if used_letters else "None yet!")
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("🔍 Current word: ", ' '.join(word_list))

        user_letter = input("🎯 Take a guess! Pick a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("🎊 Great choice! Keep going! 🎊")
            else:
                lives -= 1  
                print(f"😢Sorry! {user_letter} is not in the word. Try again!")
        elif user_letter in used_letters:
            print("⚠️ You've already guessed that one! Try something new!")
        else:
            print("🚫 That's not a valid letter. Give it another shot!")

    if lives == 0:
        print(f"💀 Oh no, you're out of lives! The word was: {word}. Better luck next time! 💀")
    else:
        print(f"🎉 YAY! You guessed the word {word} and won the game! 🎉")

if __name__ == '__main__':
    hangman()