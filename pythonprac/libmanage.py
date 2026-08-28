# ==========================================
#      LIBRARY MANAGEMENT SYSTEM
# ==========================================

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "available": True
    },
    {
        "id": 2,
        "title": "Data Structures",
        "author": "Robert Martin",
        "available": True
    },
    {
        "id": 3,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "available": True
    }
]

members = []

borrowed_books = []


# ==========================================
# ADD BOOK
# ==========================================

def add_book():
    print("\n===== ADD BOOK =====")

    book_id = len(books) + 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book added successfully!")


# ==========================================
# VIEW ALL BOOKS
# ==========================================

def view_books():
    print("\n===== ALL BOOKS =====")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        status = "Available" if book["available"] else "Borrowed"

        print(
            f"ID: {book['id']} | "
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Status: {status}"
        )


# ==========================================
# SEARCH BOOK
# ==========================================

def search_book():
    print("\n===== SEARCH BOOK =====")

    search = input("Enter book title or author: ").lower()

    found = False

    for book in books:
        if (
            search in book["title"].lower()
            or search in book["author"].lower()
        ):
            status = "Available" if book["available"] else "Borrowed"

            print(
                f"\nID: {book['id']}"
                f"\nTitle: {book['title']}"
                f"\nAuthor: {book['author']}"
                f"\nStatus: {status}"
            )

            found = True

    if not found:
        print("Book not found,please make it happen.")


# ==========================================
# REGISTER MEMBER
# ==========================================

def register_member():
    print("\n===== REGISTER MEMBER =====")

    member_id = len(members) + 1
    name = input("Enter member name: ")
    email = input("Enter email: ")

    member = {
        "id": member_id,
        "name": name,
        "email": email
    }

    members.append(member)

    print("Member registered successfully!")
    print(f"Member ID: {member_id}")


# ==========================================
# VIEW MEMBERS
# ==========================================

def view_members():
    print("\n===== ALL MEMBERS =====")

    if len(members) == 0:
        print("No members registered.")
        return

    for member in members:
        print(
            f"ID: {member['id']} | "
            f"Name: {member['name']} | "
            f"Email: {member['email']}"
        )


# ==========================================
# BORROW BOOK
# ==========================================

def borrow_book():
    print("\n===== BORROW BOOK =====")

    if len(members) == 0:
        print("Please register a member first.")
        return

    view_books()

    try:
        book_id = int(input("\nEnter book ID: "))
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Find book
    selected_book = None

    for book in books:
        if book["id"] == book_id:
            selected_book = book
            break

    if selected_book is None:
        print("Book not found.")
        return

    # Check availability
    if not selected_book["available"]:
        print("Sorry, this book is already borrowed.")
        return

    # Find member
    selected_member = None

    for member in members:
        if member["id"] == member_id:
            selected_member = member
            break

    if selected_member is None:
        print("Member not found.")
        return

    # Mark book as borrowed
    selected_book["available"] = False

    borrowed = {
        "book_id": book_id,
        "book_title": selected_book["title"],
        "member_id": member_id,
        "member_name": selected_member["name"]
    }

    borrowed_books.append(borrowed)

    print("\nBook borrowed successfully!")
    print(f"Book: {selected_book['title']}")
    print(f"Member: {selected_member['name']}")


# ==========================================
# RETURN BOOK
# ==========================================

def return_book():
    print("\n===== RETURN BOOK =====")

    if len(borrowed_books) == 0:
        print("No books are currently borrowed.")
        return

    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    # Find borrowed book
    borrowed_book = None

    for borrowed in borrowed_books:
        if borrowed["book_id"] == book_id:
            borrowed_book = borrowed
            break

    if borrowed_book is None:
        print("This book is not currently borrowed.")
        return

    # Make book available again
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            break

    # Remove borrowing record
    borrowed_books.remove(borrowed_book)

    print("\nBook returned successfully!")
    print(f"Book: {borrowed_book['book_title']}")
    print(f"Returned by: {borrowed_book['member_name']}")


# ==========================================
# VIEW BORROWED BOOKS
# ==========================================

def view_borrowed_books():
    print("\n===== BORROWED BOOKS =====")

    if len(borrowed_books) == 0:
        print("No books are currently borrowed.")
        return

    for borrowed in borrowed_books:
        print(
            f"Book ID: {borrowed['book_id']} | "
            f"Book: {borrowed['book_title']} | "
            f"Member: {borrowed['member_name']}"
        )


# ==========================================
# REMOVE BOOK
# ==========================================

def remove_book():
    print("\n===== REMOVE BOOK =====")

    try:
        book_id = int(input("Enter book ID to remove: "))
    except ValueError:
        print("Please enter a valid book ID.")
        return

    for book in books:
        if book["id"] == book_id:

            if not book["available"]:
                print("You cannot remove a borrowed book.")
                return

            books.remove(book)

            print("Book removed successfully!")
            return

    print("Book not found.")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. View Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. View Borrowed Books")
        print("9. Remove Book")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            register_member()

        elif choice == "5":
            view_members()

        elif choice == "6":
            borrow_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            view_borrowed_books()

        elif choice == "9":
            remove_book()

        elif choice == "10":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# ==========================================
# START PROGRAM
# ==========================================

main()