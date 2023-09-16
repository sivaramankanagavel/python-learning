"""
Here we are going to do the library app:
1. Add the library Books.
2. Make the list for available books.
3. ask user to pick book which one he/she want from library
4. if user return the book then add it on the available book list.
5. Show the lended book list.
6. quit option
"""


class Library:

    def __init__(self, user_name, books_list):
        self.user_name = user_name
        self.book_list = books_list
        self.available_books = books_list.copy()
        self.lended_books = []  # key-user_name & value-book_name

    def get_book_list(self):
        return self.book_list

    def get_available_books(self):
        return self.available_books

    def lend_book(self, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.lended_books.append({"user_name": self.user_name, "book_name": book_name})
            return self.lended_books

    def returned_book_update(self, book_name):
        new_lended_book_list = []
        self.available_books.append(book_name)
        for book in self.lended_books:
            if book["book_name"] != book_name:
                new_lended_book_list.append(book)

        self.lended_books.clear()
        self.lended_books = new_lended_book_list
        return self.lended_books

    def library_services(self):
        print("\nWelcome to the Siva's Library !!!! \nHow can I help you ?, kindly choose the below service :")
        while True:
            print("\n 1. get book list\n 2. get available books\n 3. Lend book \n 4. Return lended book"
                  "\n 5. Show the lended books list  \n6. Exit")
            service_request = int(input("Enter the service you want: "))

            if service_request == 1:
                print(self.get_book_list())
            if service_request == 2:
                print(self.get_available_books())
            if service_request == 3:
                user_want_book = input("Enter the book name you want based on available books: ")
                print(self.lend_book(book_name=user_want_book))
            if service_request == 4:
                return_book = input("Which Book you want to return: ")
                print(self.returned_book_update(book_name=return_book))
            if service_request == 5:
                print(self.lended_books)
            if service_request == 6:
                print("Thanks for visiting our Library 🙏🙏🙏")
                break