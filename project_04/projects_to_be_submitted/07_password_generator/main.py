import random
import time

def generate_passwords(amount, length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%&*?"
    passwords = ["".join(random.choice(chars) for _ in range(length)) for _ in range(amount)]
    return passwords

def main():
    print("\n🔐 Welcome to Your Ultimate Password Generator! 🔐\n")
    
    try:
        number = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the desired password length: "))
        
        if number <= 0 or length <= 0:
            print("\n⚠️ Please enter positive numbers only! Try again. ⚠️")
            return
        
        print("\nGenerating your secure passwords...🔄")
        time.sleep(1)
        
        passwords = generate_passwords(number, length)
        print("\n✨ Here are your secure passwords ✨\n")
        for index, password in enumerate(passwords, start=1):
            print(f"{index}. {password}")
        
        print("\n✅ Done! Keep them safe! ✅")
    
    except ValueError:
        print("\n🚫 Invalid input! Please enter numbers only. 🚫")

if __name__ == "__main__":
    main()
