# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def count_numbers():
    number_counts = {}  
    
    while True:
        try:
            num = input("Enter a number (or press Enter to stop): ")
            if num == "":  
                break
            num = int(num)  
            
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1
        except ValueError:
            print("Please enter a valid number.")
    
    for num, count in number_counts.items():
        print(f"{num} appears {count} times.")


count_numbers()
