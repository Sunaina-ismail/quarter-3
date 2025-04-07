# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.
# Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects the returned name to be Sophia):
# Howdy Sophia ! 🤠

def get_name():
    """Returns the name as a string."""
    return "Sophia"

def main():
    """Calls get_name() and prints a greeting."""
    name = get_name()
    print("Howdy", name, "! 🤠")

main()
