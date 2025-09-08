# Library Management System

books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"title": title, "author": author})
    print("📚 Book added successfully!")

def remove_book():
    title = input("Enter book title to remove: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("❌ Book removed successfully!")
            return
    print("⚠️ Book not found!")

def view_books():
    if not books:
        print("⚠️ No books available!")
    else:
        print("\n--- Library Books ---")
        for book in books:
            print(f"Title: {book['title']} | Author: {book['author']}")

def search_book():
    title = input("Enter book title to search: ")
    for book in books:
        if book["title"].lower() == title.lower():
            print(f"✅ Book Found: {book['title']} by {book['author']}")
            return
    print("⚠️ Book not found!")

def menu():
    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice!")

menu()
