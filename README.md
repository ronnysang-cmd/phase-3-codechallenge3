# Library Management System

## Classes

### Author
- Has name and list of books
- Methods: `add_book()`, `total_books()`, `books_by_genre()`

### Book  
- Has title, genre, author, and borrowed_by
- Methods: `is_available()`, `borrow()`, `return_book()`

### Member
- Has name and borrowed_books list
- Methods: `borrow_book()`, `return_book()`, `books_count()`, `books_by_author()`

### Library
- Has name, books list, and members list
- Methods: `add_book()`, `add_member()`, `available_books()`, `borrowed_books()`, `books_by_genre()`, `books_by_author()`, `most_active_member()`, `most_popular_genre()`

## How to run
```
python3 test_library.py
```

## Features
- Object relationships between classes
- Aggregate methods that work with collections
- Association methods for borrowing system# phase-3-codechallenge3
