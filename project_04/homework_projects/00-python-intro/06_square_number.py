# Ask the user for a number and print its square (the product of the number times itself).
# Here's a sample run of the program (user input is in bold italics):
# Type a number to see its square: 4
# 4.0 squared is 16.0


def square():
    number = int(input("Enter a number to find its Square: "))
    square_number = number ** 2
    
    print(f"The square of the number is {square_number}")
    
square()