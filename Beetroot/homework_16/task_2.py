class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        Book.total_books += 1
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library({self.name}, {len(self.books)} books, {len(self.authors)} authors)"

    def __str__(self):
        return f"{self.name} library with {len(self.books)} books and {len(self.authors)} authors"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author.name})"

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday}, {len(self.books)} books)"

    def __str__(self):
        return f"{self.name} ({self.birthday}), {self.country}, author of {len(self.books)} books"


my_library = Library("Library")

george_martin = Author("George R. R. Martin", "New Jersey", 1948)
tolkien = Author("John Ronald Reuel Tolkien", "Bloemfontein", 1920)

new_book = my_library.new_book("A Game of Thrones", 1991, george_martin)
new_book_first = my_library.new_book("A Clash of Kings", 1998, george_martin)
new_book_second = my_library.new_book("A Storm of Swords", 2000, george_martin)
new_book_tree = my_library.new_book("The Fellowship of the Ring", 1954, tolkien)
new_book_four = my_library.new_book("The Two Towers", 1954, tolkien)
new_book_five = my_library.new_book("The Return of the King", 1955, tolkien)

print(my_library.books)
print(my_library.group_by_author(george_martin))
print(my_library.group_by_author(tolkien))
print(Book.total_books)
print(my_library.group_by_year(1954))