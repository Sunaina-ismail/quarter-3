import json

LIBRARY_FILE = "library.txt"

def load_library():
    """Load library data from file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def print_separator():
    print(" " * 50)

def add_book(library):
    """Add a book to the library."""
    print_separator()
    print("📚 ADD A NEW BOOK 📚")
    print_separator()
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    publication_year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": int(publication_year),
        "genre": genre,
        "read": read_status
    })
    print("\n✅ Book added successfully! ✅\n")

def remove_book(library):
    """Remove a book from the library."""
    print_separator()
    print("❌ REMOVE A BOOK ❌")
    print_separator()
    title = input("Enter the title of the book to remove: ").strip()
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("\n✅ Book removed successfully! ✅\n")
            return
    print("\n⚠️ Book not found! ⚠️\n")

def search_book(library):
    """Search for a book by title or author."""
    print_separator()
    print("🔍 SEARCH FOR A BOOK 🔍")
    print_separator()
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter search keyword: ").strip().lower()
    
    matches = [book for book in library if 
               (choice == "1" and keyword in book["title"].lower()) or
               (choice == "2" and keyword in book["author"].lower())]
    
    print_separator()
    if matches:
        print("📖 Matching Books 📖")
        for book in matches:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        print("⚠️ No matching books found! ⚠️")
    print_separator()
    print()

def display_books(library):
    """Display all books in the library."""
    print_separator()
    print("📚 YOUR LIBRARY 📚")
    print_separator()
    if not library:
        print("⚠️ Your library is empty! ⚠️\n")
        return
    
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    print_separator()
    print()

def display_statistics(library):
    """Display statistics of the library."""
    print_separator()
    print("📊 LIBRARY STATISTICS 📊")
    print_separator()
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"📚 Total books: {total_books}")
    print(f"✅ Books read: {read_books}")
    print(f"📈 Percentage read: {percentage_read:.2f}%\n")
    print_separator()

def main():
    """Main function to run the library manager."""
    library = load_library()
    
    while True:
        print_separator()
        print("📚 Welcome to Your Personal Library Manager! 📚")
        print_separator()
        print("1 Add a book")
        print("2 Search for a book")
        print("3 Display all books")
        print("4 Display statistics")
        print("5 Remove a book")
        print("6 Exit")
        print_separator()
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n💾 Library saved successfully. Goodbye! 👋\n")
            print_separator()
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 6. ⚠️\n")
            print_separator()

if __name__ == "__main__":
    main()