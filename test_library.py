from library_system import Author, Book, Member, Library

library = Library("My Library")

author1 = Author("George Orwell")
author2 = Author("Jane Austen")

book1 = Book("1984", "Fiction")
book2 = Book("Animal Farm", "Fiction")
book3 = Book("Pride and Prejudice", "Romance")

author1.add_book(book1)
author1.add_book(book2)
author2.add_book(book3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member("Alice")
member2 = Member("Bob")

library.add_member(member1)
library.add_member(member2)

print(f"Available books: {len(library.available_books())}")
member1.borrow_book(book1)
member2.borrow_book(book2)

print(f"Available books after borrowing: {len(library.available_books())}")
print(f"Borrowed books: {len(library.borrowed_books())}")

print(f"Author1 total books: {author1.total_books()}")
print(f"Alice's book count: {member1.books_count()}")
print(f"Most active member: {library.most_active_member().name}")
print(f"Most popular genre: {library.most_popular_genre()}")

member1.return_book(book1)
print(f"Available books after return: {len(library.available_books())}")