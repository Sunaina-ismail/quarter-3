# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.



def subtract_seven(num):
    """Subtracts 7 from the given number."""
    return num - 7

def main():
    """Prompts the user for a number, subtracts 7, and prints the result."""
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)


main()
