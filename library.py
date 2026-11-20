class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: '{book.title}' to {self.name}.")

    def list_books(self):
        print(f"\n--- Books in {self.name} ---")
        for book in self.books:
            print(book)
        print("---------------------------\n")

    def borrow_book(self, title):
        # Search for the requested book by title
        for book in self.books:
            if book.title.lower() == title.lower():
                # If found, check whether it is available
                if book.is_borrowed:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"Successfully borrowed '{book.title}'.")
                return

        # If the loop finishes, the book was not found
        print(f"Error: '{title}' was not found in {self.name}.")

if __name__ == "__main__":
    my_library = Library("City Central Library")
    
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    
    my_library.list_books()
