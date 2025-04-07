# In this program we show an example of using dictionaries to keep track of information in a phonebook.



def phonebook():
    contacts = {}  
    
    while True:
        name = input("Enter contact name (or press Enter to stop): ")
        if name == "":
            break
        number = input("Enter phone number: ")
        contacts[name] = number
    
    print("\nPhonebook:")
    for name, number in contacts.items():
        print(f"{name}: {number}")
    
    while True:
        search_name = input("Enter a name to search (or press Enter to stop): ")
        if search_name == "":
            break
        print(contacts.get(search_name, "Contact not found."))

# Run the function
phonebook()
