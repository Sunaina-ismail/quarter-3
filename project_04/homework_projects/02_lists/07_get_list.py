# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']









def get_values():
    list = []  

    while True:
        value = input("Enter a value (press enter to stop): ")
        if not value:  
            break
        list.append(value)  

    print("Here's the list:", list)

get_values()
