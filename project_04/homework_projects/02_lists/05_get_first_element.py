# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.








def print_first_item(items):
    print(items[0])
def collect_items():
    """
    Continuously collects items from the user until they press enter, then returns the list.
    """
    items = []
    while True:
        entry = input("Enter an item for the list (press enter to finish): ")
        if not entry:
            break
        items.append(entry)
    return items


items = collect_items()
print_first_item(items)





