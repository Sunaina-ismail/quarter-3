# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.
 # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
# Print the length of the list.
# Add 'mango' at the end of the list. 
# Print the updated list.

# def main():
#     fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
#     print(fruit_list)
    
#     length_of_list = len(fruit_list)
#     print("The length of the fruit list is :", length_of_list)
    
#     fruit_list.append("Moango")
    
#     print("The Updated list of fruits:",fruit_list)
    
# main()


# Practice #02 Index Game Solution
def access_element(lst, index):
   
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

def modify_element(lst, index, new_value):
  
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

def slice_list(lst, start, end):
    
    if start < 0 or end > len(lst):
        return "Invalid indices."
    return lst[start:end]

def index_game():
    lst = [1, 2, 3, 4, 5]  
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()



