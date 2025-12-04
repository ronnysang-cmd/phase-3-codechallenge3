class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        book.author = self
    
    def total_books(self):
        return len(self.books)
    
    def books_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]


class Book:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.author = None
        self.borrowed_by = None
    
    def is_available(self):
        return self.borrowed_by is None
    
    def borrow(self, member):
        if self.is_available():
            self.borrowed_by = member
            member.borrowed_books.append(self)
    
    def return_book(self):
        if self.borrowed_by:
            self.borrowed_by.borrowed_books.remove(self)
            self.borrowed_by = None


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        book.borrow(self)
    
    def return_book(self, book):
        book.return_book()
    
    def books_count(self):
        return len(self.borrowed_books)
    
    def books_by_author(self, author):
        return [book for book in self.borrowed_books if book.author == author]


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def available_books(self):
        return [book for book in self.books if book.is_available()]
    
    def borrowed_books(self):
        return [book for book in self.books if not book.is_available()]
    
    def books_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]
    
    def books_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def most_active_member(self):
        if not self.members:
            return None
        return max(self.members, key=lambda m: m.books_count())
    
    def most_popular_genre(self):
        borrowed = self.borrowed_books()
        if not borrowed:
            return None
        genres = {}
        for book in borrowed:
            genres[book.genre] = genres.get(book.genre, 0) + 1
        return max(genres, key=genres.get)