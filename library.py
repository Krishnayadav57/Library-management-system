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
                    book_id, title, author, quantity = line.split()

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
    
users_dict = load_user()
# print(users_dict)
register_user(users_dict)
##register_user(users_dict,user)
