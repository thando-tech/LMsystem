#Rewrite the entire task 1 and task 1B without using parameters and arguments in your functions.


#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []

# The system features two functions (You must create these functions): add_book and add_member. 
#The add_bookfunction takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list. 
def add_book():
    books.append({
        "book_id": int(input("Enter the book ID: ")),
        "title": input("Enter a book title: "),
        "author": "Hope",
        "status": "Available"
    })

    # The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list. 
    #Each member dictionary includes an mpty list for borrowed_books to track the IDs of books each member has borrowed
def add_member():
    members.append({
        "member_id": 1234,
        "name": "Langelihle",
        "borrowed_books": []
    })


    # Add a book and a member
add_book()
add_member()

# Print both lists
print("Books:", books)
print("Members:", members)