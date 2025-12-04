"""
Libarary management system
(register, login) --> user
(add book, issue book, return book, view book, search book)

"""

### Creating two file named users.txt and books.txt to store user information and books information permanently inside the file. 


import os

if not os.path.exists('users.txt'):
    with open('users.txt', 'w') as f:
        pass

if not os.path.exists('books.txt'):
    with open('books.txt', 'w') as f:
        pass

### load data from the file 
def load_user():
    '''Load all the user from users.txt into dictionary'''
    users_dict = {}

    try:
        with open('users.txt', 'r') as f:
             for line in f:
                 line = line.strip()
                 if line:
                     username, password = line.split(',')
                     users_dict[username] = password

    except FileNotFoundError:
        print("File not Found!")

    return users_dict

def load_books():
    books_list = []
    try:
        with open("books.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    book_id, title, author, quantity = line.split(',')

                    book = {
                        'id' : book_id,
                        'title' : title,
                        'author' : author,
                        'quantity' : int(quantity)
                    }
                    books_list.append(book)

    except FileNotFoundError:
        print("Files not find!")
    return books_list

def get_existing_books_id(books_list):
    '''Create a set to store all the ids of the books'''
    book_ids = set()
    for books in books_list:
        #Dictionary
        book_ids.add(books['id'])
    return book_ids
    
#### user registraton
def register_user(users_dict):
    '''Reading a new user'''
    print("\n-----Register a New User-----")
    username = input("Enter the Username :- ").strip()
    password = input("Enter Password :- ").strip()
    if username in users_dict:
        print(f"username already exist!")
        return False
    if not username or not password:
        print("Username and Password cannot be empty!")
        return False
    users_dict[username] = password

    ###save the registered user to the file 'users.txt'
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

        print("Registration successful!")
        return True
    
# users_dict = load_user()
# print(users_dict)
# register_user(users_dict)
# login_user(load_user)
##register_user(users_dict,user)


def login_user(users_dict):
    print("\n-------Login User-------")
    username = input("Enter username :- ").strip()
    password = input("Enter password :- ").strip()

    if username in users_dict and users_dict[username] == password:
        print(f"Welcome! {username.capitalize()}")
        return username
    else:
        print(f"Invalid username or password!!!")
        return None
    
# login_user(users_dict)

##NOw book operation is start
## Main menu Function

def main_menu():
    '''Display main menu option'''
    print("="*55)
    print("\nLibrary Management system")
    print("="*55)
    print("1. ADD book")
    print("2. View All Book")
    print("3. search book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Logout")
    print("="*55)

# main_menu()

## ADD BOOK 
def add_book(books_list, book_ids):
    '''Add a new book to the library'''
    print("\n-------ADD NEW BOOK------")
    book_id = input("Enter the book id :- ").strip()

    if book_id in book_ids:
        print("Book already exists!!")
        return
    
    title = input("Enter the book title :- ").strip()
    author = input("Enter the book author :- ").strip()
    quantity = int(input("Enter the book quantity :- ").strip())

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }

    books_list.append(new_book)
    book_ids.add(book_id)

    with open("books.txt", "a") as f:
        f.write(f"{book_id},{title},{author},{quantity}\n")

    print("Book added sucesseful")

book_dict = load_books()
# books_ids = get_existing_books_id(book_dict)
# print(book_dict)
# print(books_ids)
# add_book(book_dict,books_ids)

def view_books(books_list):
    '''Display all the books in the library'''
    print("\n-----All book in library")
    if not books_list:
        print("No books found!! in library")
        return
    for book in books_list:
        print(f"{book['id']} | {book['title']} | {book['author']} | {book['quantity']}")

# book_dict = load_books()
# view_books(book_dict)

# Load everything
users_dict = load_user()
books_list = load_books()
book_ids = get_existing_books_id(books_list)

# # Example: Login
login_user(users_dict)

# # Example: Add a book
# add_book(books_list, book_ids)

# # View books
# view_books(books_list)
