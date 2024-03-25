#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []

# The system features two functions (You must create these functions): add_book and add_member. 
#The add_bookfunction takes three parameters (book_id, title, author, status) and appends a new book dictionary to the books list. 
def add_book(book_id, title, author, status):
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

    # The add_member function, on the other hand, requires two parameters (member_id, name) and appends a new member dictionary to the members list. 
    #Each member dictionary includes an mpty list for borrowed_books to track the IDs of books each member has borrowed
def add_member(member_id, name):
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })


    # Add a book and a member
add_book(2024001, "Python Programming", "Jacob Zuma", "Available")
add_member(1, "Anelisa Maleka")

# Print both lists
print("Books:", books)
print("Members:", members)