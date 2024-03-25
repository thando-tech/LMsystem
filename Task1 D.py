#Rewrite the entire Task 1 C using Data frames instead of lists.
import pandas as pd

bookDetails = ({
        "book_id": [int(input("Enter the book ID: "))],
        "title": [input("Enter a book title: ")],
        "author": ["Hope"],
        "status": ["Available"]
    })

dfBooks = pd.DataFrame(bookDetails)


print("Data Frame for books: ", dfBooks)


membersDetails = ({
        "member_id": [1234],
        "name": ["Langelihle"],
        "borrowed_books": []
    })

dfMembers = pd.DataFrame(membersDetails)

print("Data frame for members: ",dfMembers)


