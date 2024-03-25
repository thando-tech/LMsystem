#Rewrite the entire task 1B without using functions


#Initialize two data structures to keep track of books and members both represented as lists
books = []
members = []


bookDetails = ({
        "book_id": int(input("Enter the book ID: ")),
        "title": input("Enter a book title: "),
        "author": "Hope",
        "status": "Available"
    })

books.append(bookDetails)



membersDetails = ({
        "member_id": 1234,
        "name": "Langelihle",
        "borrowed_books": []
    })

members.append(membersDetails)



# Print both lists
print("Books:", books)
print("Members:", members)