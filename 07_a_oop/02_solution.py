class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def display_books(self):
        print(self.book_list)

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
        else:
            print("Book not found")

my_library = Library()
my_library.add_book("1984")
my_library.add_book("Godan")
my_library.add_book("Kavyanchal")
my_library.display_books()
my_library.remove_book("Kavyancha")
my_library.display_books()