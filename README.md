📚 Library Management System (Python)

A simple, CLI-based Library Management System built using Python.
The application supports user registration, login, adding books, issuing books, returning books, viewing, and searching books.
All data is stored persistently in text files (users.txt and books.txt).

⭐ Features
👤 User Management

Register new users

Login with existing credentials

Username–password storage in users.txt

📘 Book Management

Add new books

View all available books

Search books by title or author

Issue books (decrease quantity)

Return books (increase quantity)

Persistent storage in books.txt

🗂 Storage Format

users.txt → username,password

books.txt → book_id,title,author,quantity

🧩 How It Works
1. File Initialization

If users.txt or books.txt do not exist, the program automatically creates them.

2. User Flow

Users begin by selecting:

1. Register
2. Login
3. Exit


Once logged in, users can access the main library menu:

1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Logout

📂 Project Structure
Library-Management-System/
│── main.py
│── users.txt
│── books.txt
│── README.md   ← (you are here)

▶️ Running the Program
1️⃣ Clone the repository
git clone https://github.com/Krishnayadav57/library-management-system.git
cd your-repo-name

2️⃣ Run the script
python main.py

🛠️ Code Overview
🔹 User Functions
Function	Description
load_user()	Loads all users from users.txt
register_user()	Registers new users
login_user()	Authenticates a user
🔹 Book Functions
Function	Description
load_books()	Loads book data
add_book()	Adds a new book
view_books()	Displays all books
search_books()	Search by title/author
issue_book()	Issues a book to a user
return_book()	Returns a book
save_books()	Saves updated book list to file
🔹 Program Flow

main() controls all menus, login flow, and book operations.

📝 Sample Storage Format
users.txt
john,1234
alice,pass123

books.txt
101,The Hobbit,J.R.R. Tolkien,3
102,Atomic Habits,James Clear,5

🚀 Future Improvements

Add GUI using Tkinter/PyQt

Add admin/user roles

Add book categories

Add password hashing

Replace text files with SQLite/MySQL

🤝 Contributing

Pull requests and suggestions are welcome!
Feel free to fork the repo and enhance the project.

📄 License

This project is open-source and free to use.
