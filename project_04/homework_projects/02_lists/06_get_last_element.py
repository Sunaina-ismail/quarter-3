# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.








def print_last_item(items):
    """
    Displays the last item in the given list.
    """
    print(items[-1])


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
print_last_item(items)




