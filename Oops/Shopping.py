# Book Class:
# Attributes: title, author, isbn, is_available (boolean to indicate if the book is available).
# Methods: __str__ (to display book details).
# Library Class:
    # Attributes: books (a list to store books).

# Methods:
    # add_book(book): Add a book to the library.
    # remove_book(isbn): Remove a book by ISBN.
    # search_by_title(title): Search for books by title.
    # search_by_author(author): Search for books by author.
    # display_books(): Display all books in the library.
# class Book():
#     def __init__(self,title,author,quantity,isbn,is_available):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#         self.quantity=quantity
#         self.is_available=is_available
# class Library(Book):
#     self.books_list=[]
#     def add_book(self,book):
#         for item in self.books_list:
#             if item.title==book:
#                 item.quantity+=1
#                 break
#         else:
#             self.books_list.append(book)
#     def remove_book(self,book):
#         for item in self.books_list:
#             if item.title==book:
#                 self.books_list.remove(book)
#             else:
#                 print("Book Not found to remove")
#     def search_by_title(self,title):
#         for item in self.books_list:
#             if item.title==title:
#                 print(item)
#         else:
#             print("Book with title not found")
#     def display_books(self):
#         for item in self.books_list:
#             print(f"-{item}")
# newQuestion
# Library Items:
    # The library manages different types of items, such as books and magazines.
    # Each item has common attributes like title, author, isbn, and quantity.
    # Each item type has additional unique attributes (e.g., Magazine has an issue_number).
# Members:
    # Members can borrow and return library items.
    # Each member has a member_id, name, and a list of borrowed items.
# Library:
    # The library maintains a list of all items and members.
    # It provides functionality to:
    # Add or remove items
    # Register or remove members.
    # Allow members to borrow and return items.
    # Display all items or search for items by title.
from abc import ABC, abstractmethod

# Abstract Base Class for Library Items
class LibraryItem(ABC):
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    @abstractmethod
    def display_info(self):
        pass

# Book Class (Inherits from LibraryItem)
class Book(LibraryItem):
    def display_info(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"

# Magazine Class (Inherits from LibraryItem)
class Magazine(LibraryItem):
    def __init__(self, title, author, isbn, quantity, issue_number):
        super().__init__(title, author, isbn, quantity)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine: {self.title} by {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}, Issue: {self.issue_number}"

# Member Class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.quantity > 0:
            self.borrowed_items.append(item)
            item.quantity -= 1
            print(f"{self.name} borrowed '{item.title}'")
        else:
            print(f"'{item.title}' is out of stock.")

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.quantity += 1
            print(f"{self.name} returned '{item.title}'")
        else:
            print(f"'{item.title}' was not borrowed by {self.name}.")

# Library Class
class Library:
    def __init__(self):
        self.items = []
        self.users = []

    def add_item(self, item):
        for existing_item in self.items:
            if existing_item.isbn == item.isbn:
                existing_item.quantity += item.quantity
                print(f"Updated quantity of '{item.title}'")
                return
        self.items.append(item)
        print(f"Added new item: '{item.title}'")

    def remove_item(self, isbn):
        for item in self.items:
            if item.isbn == isbn:
                self.items.remove(item)
                print(f"Removed item: '{item.title}'")
                return
        print("Item not found.")

    def register_user(self, member):
        for user in self.users:
            if user.member_id == member.member_id:
                print("User already exists.")
                return
        self.users.append(member)
        print(f"Registered new user: {member.name}")

    def remove_user(self, member_id):
        for user in self.users:
            if user.member_id == member_id:
                self.users.remove(user)
                print(f"Removed user: {user.name}")
                return
        print("User not found.")

    def borrow_item(self, member_id, isbn):
        member = self._find_member(member_id)
        if not member:
            print("User not found.")
            return

        item = self._find_item(isbn)
        if not item:
            print("Item not found.")
            return

        member.borrow_item(item)

    def return_item(self, member_id, isbn):
        member = self._find_member(member_id)
        if not member:
            print("User not found.")
            return

        item = self._find_item(isbn)
        if not item:
            print("Item not found.")
            return

        member.return_item(item)

    def display_items(self):
        if not self.items:
            print("No items in the library.")
            return
        for item in self.items:
            print(item.display_info())

    def display_borrowed_items(self, member_id):
        member = self._find_member(member_id)
        if not member:
            print("User not found.")
            return

        if not member.borrowed_items:
            print(f"{member.name} has no borrowed items.")
            return

        print(f"{member.name}'s borrowed items:")
        for item in member.borrowed_items:
            print(item.display_info())

    def _find_member(self, member_id):
        for user in self.users:
            if user.member_id == member_id:
                return user
        return None

    def _find_item(self, isbn):
        for item in self.items:
            if item.isbn == isbn:
                return item
        return None




