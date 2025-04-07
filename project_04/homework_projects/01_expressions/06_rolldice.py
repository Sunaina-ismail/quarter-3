# Simulate rolling two dice, and prints results of each roll as well as the total.



import random  

NUM_SIDES = 6  

def roll_dice():
    """Simulates rolling two dice and prints the result."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(f"Each die has {NUM_SIDES} sides.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    roll_dice()
