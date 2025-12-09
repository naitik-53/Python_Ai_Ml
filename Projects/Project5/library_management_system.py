# “Library Management System (Without Files)”

# ➡ Pure Python logic
# ➡ Functions + dict + loops + conditions + sets ka full use
# ➡ Real-life system jaisa

# Isme hoga:

# Book add

# Book remove

# Book search

# Borrow/Return

# Current borrowed books

# Unique categories (sets se)

# All data dictionaries me hoga

# STEP 1 — System ka Data Structure
library = {
    "books": [],         # List of dictionaries
    "borrowed": {},      # username -> list of books
    "categories": set()  # unique categories
}

# STEP 2 — Add Book Function
def add_book(title, author, category):
    book = {
        "title": title,
        "author": author,
        "category": category
    }
    library["books"].append(book)
    library["categories"].add(category)
    print("Book added successfully!")

# STEP 3 — Remove Book
def remove_book(title):
    for book in library["books"]:
        if book["title"].lower() == title.lower():
            library["books"].remove(book)
            print("Book removed!")
            return
    print("Book not found!")

# STEP 4 — Search Book
def search_book(keyword):
    result = []
    for book in library["books"]:
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            result.append(book)
    return result

# STEP 5 — Borrow Book
def borrow_book(username, title):
    for book in library["books"]:
        if book["title"].lower() == title.lower():
            library["books"].remove(book)
            library["borrowed"].setdefault(username, []).append(book)
            print(f"{username} borrowed {title}")
            return
    print("Book not available!")

# STEP 6 — Return Book
def return_book(username, title):
    if username not in library["borrowed"]:
        print("User has no borrowed books!")
        return

    for book in library["borrowed"][username]:
        if book["title"].lower() == title.lower():
            library["borrowed"][username].remove(book)
            library["books"].append(book)
            print(f"{username} returned {title}")
            return

    print("Book not found in borrowed list!")

# STEP 7 — Show All Books
def show_books():
    if not library["books"]:
        print("No books available!")
        return

    for book in library["books"]:
        print(f"{book['title']} — {book['author']} ({book['category']})")

# FINAL — Main Menu System (Pure Python)
while True:
    print("\n=== Library System ===")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show All Books")
    print("7. Show Categories")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book(input("Title: "), input("Author: "), input("Category: "))

    elif choice == "2":
        remove_book(input("Book title to remove: "))

    elif choice == "3":
        result = search_book(input("Keyword: "))
        for r in result:
            print(r)

    elif choice == "4":
        borrow_book(input("Username: "), input("Book title: "))

    elif choice == "5":
        return_book(input("Username: "), input("Book title: "))

    elif choice == "6":
        show_books()

    elif choice == "7":
        print("Categories:", library["categories"])

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")