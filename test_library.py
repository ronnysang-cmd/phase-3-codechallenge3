from library_system import Author, Book, Member, Library

# Create library
library = Library("My Library")

# Create authors
author1 = Author("George Orwell")
author2 = Author("Jane Austen")

# Create books
book1 = Book("1984", "Fiction")
book2 = Book("Animal Farm", "Fiction")
book3 = Book("Pride and Prejudice", "Romance")

# Add books to authors
author1.add_book(book1)
author1.add_book(book2)
author2.add_book(book3)

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create members
member1 = Member("Alice")
member2 = Member("Bob")

# Add members to library
library.add_member(member1)
library.add_member(member2)

# Test borrowing
print(f"Available books: {len(library.available_books())}")
member1.borrow_book(book1)
member2.borrow_book(book2)

print(f"Available books after borrowing: {len(library.available_books())}")
print(f"Borrowed books: {len(library.borrowed_books())}")

# Test methods
print(f"Author1 total books: {author1.total_books()}")
print(f"Alice's book count: {member1.books_count()}")
print(f"Most active member: {library.most_active_member().name}")
print(f"Most popular genre: {library.most_popular_genre()}")

# Test return
member1.return_book(book1)
print(f"Available books after return: {len(library.available_books())}")