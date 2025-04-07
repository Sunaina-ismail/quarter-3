AFFIRMATION: str = "I believe in myself and my abilities."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  
    while user_feedback != AFFIRMATION:  
        print("That was not the affirmation.")

        
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")



main()
