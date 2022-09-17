class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'Name of book {self.name} Author of the book is  {self.author}, year when it was created {self.year}'

    def __repr__(self):
        return f'EDITION OF {self.name} BY THE {self.author} YEAR {self.year}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Author {self.name} from {self.country}, author was born {self.birthday}, amount of books edition {self.books}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []


    def new_book(self, name: str, year: int, author: Author):
        newbookcreateres = Book(name=name, year=year, author=author)
        self.books.append(newbookcreateres)
        return newbookcreateres

    def group_by_author(self, author: Author):
        filteredbyautrors = []
        for book in self.books:
            if book.author == author:
                filteredbyautrors.append(book)
        return filteredbyautrors

    def group_by_year(self, year: int):
        filteredbyyears = []
        for book in self.books:
            if book.year == year:
                filteredbyyears.append(book)
        return filteredbyyears


if __name__ == '__main__':
    libraryforusers = Library(name='Library')

    lupen = Author(name='Maurice Marie Émile Leblanc', country='France', birthday='11 Dec 1864')
    artofst = Author(name='Albert Coombs Barnes', country='USA', birthday='2 Jan 1872')

    libraryforusers.new_book(name='Arsène Lupin', year=1907, author=lupen)
    libraryforusers.new_book(name='Arsène Lupin and Sherlock Holmes', year=1907, author=lupen)
    libraryforusers.new_book(name='The Art of the Steal', year=2009, author = artofst)

    print(libraryforusers.books)
    print(libraryforusers.group_by_author(artofst))
    print(libraryforusers.group_by_year(1907))
