# Katie Klein
# CSD 310
# WhatABook
# 10 May 2021

'''

This program allows WhatABook customers to view the catalog, view store
locations, and access a personal account wherein users can view and add
to their wishlist.

All data is stored in a SQL database with the following four tables:
- user
- store
- book
- wishlist

'''


''' IMPORT STATEMENTS '''
import mysql.connector
from mysql.connector import errorcode

from time import sleep


# database config object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


''' FUNCTIONS '''

def show_menu():
    '''Function to show main menu and allow selection'''

    # display header
    print("\n-- MAIN MENU --")

    # display instructions
    print("Enter a number to select one of the following options:")

    # display menu options
    print("\n  1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit Program")
    
    # get selection from user
    menu_selection = input("\n>> ")

    # while loop to ensure a valid menu option is selected
    while menu_selection not in ("1", "2", "3", "4"):
        menu_selection = input("\nINVALID INPUT: Please enter 1, 2, 3, or 4\n>> ")

    # if View Books is chosen
    if menu_selection == "1":
        show_books(cursor)

    # if View Store Locations is chosen
    if menu_selection == "2":
        show_locations(cursor)

    # if My Account is chosen
    if menu_selection == "3":
        user_id = validate_user(cursor)
        show_account_menu(cursor, user_id)

    # if Exit Program is chosen
    if menu_selection == "4":
        print("\n   Program terminated. Goodbye.")
        exit()

def show_books(cursor):
    '''Function to show all books in WhatABook catalog'''

    # print header
    print("\n-- BOOK CATALOG --\n")
    
    # SQL query to show contents from book table
    cursor.execute("SELECT book_name, author, details, book_id" +
                    " FROM book ORDER BY book_name")
    books = cursor.fetchall()
    for book in books:
        print(f"Title: {book[0]}\nAuthor: {book[1]}\nDetails: {book[2]}\n")

    # end of catalog message
    print("-- END OF CATALOG --")

    # show navigation options (main menu or exit)
    show_navigation()

def show_locations(cursor):
    '''Function to show all WhatABook store locations'''

    # print header
    print("\n-- WHATABOOK STORE LOCATIONS --\n")

    # SQL query to show contents from store table
    cursor.execute("SELECT locale FROM store")
    stores = cursor.fetchall()
    for store in stores:
        print(f"Address: {store[0]}\n")

    # display end of list message
    print("-- END OF STORE LIST --")

    # show navigation options (main menu or exit)
    show_navigation()

def validate_user(cursor):
    '''Function to validate user_id against user table in database'''

    # display header
    print("\n-- ACCOUNT LOGIN --\n")

    # SQL query to get all user_ids and append to list of strings
    cursor.execute("SELECT user_id FROM user")
    user_id_list = []
    query_results = cursor.fetchall()
    for row in query_results:
        user_id_list.append(str(row[0])) # user_ids stored as strings

    # prompt for user_id
    user_id = input("Enter your user_id number:\n>> ")

    # while loop to ensure input user_id is in list of all user_ids
    while (user_id not in user_id_list):
        user_id = input("\nINVALID INPUT: Please enter a valid user_id number:\n>> ")

    # display success message
    print("\nThank you, user_id accepted.\n")

    # pause before displaying account information
    sleep(1)

    # return user_id for use in account menu
    return user_id

def show_account_menu(cursor, user_id):
    '''Function to show account menu options and allow selection'''

    # get first name of user
    cursor.execute("SELECT first_name FROM user" +
                    " WHERE user_id = " + str(user_id))
    first_name = cursor.fetchall()
    
    # print account header customized with user's first name
    for name in first_name:
        print(f"-- {name[0].upper()}'S ACCOUNT --")

    # show account menu options
    print("  1. Wishlist\n  2. Add Book\n  3. Main Menu")

    # store user input
    menu_selection = input("\n>> ")
    
    # while loop to ensure a valid menu option is selected
    while menu_selection not in ("1", "2", "3"):
        menu_selection = input("\nINVALID INPUT: Please enter 1, 2, or 3\n>> ")

    # if View Wishlist is selected
    if menu_selection == "1":
        show_wishlist(cursor, user_id)
    
    # if Add Book is selected
    if menu_selection == "2":
        book_id = show_books_to_add(cursor, user_id)
        add_book_to_wishlist(cursor, user_id, book_id)
    
    # if Main Menu is selected
    if menu_selection == "3":
        show_menu()

def show_wishlist(cursor, user_id):
    '''Function to show a specific user's wishlist'''

    # display header
    print("\n-- WISHLIST --\n")
    
    # get user's wishlist
    cursor.execute("SELECT book.book_name, book.author" +
                    " FROM book" +
                    " INNER JOIN wishlist ON book.book_id = wishlist.book_id" +
                    " INNER JOIN user ON wishlist.user_id = user.user_id" +
                    " WHERE user.user_id = " + user_id)

    user_wishlist = cursor.fetchall()
    
    # print user's wishlist
    for row in user_wishlist:
        print(f"Title: {row[0]}")
        print(f"Author: {row[1]}\n")

    # display end of list message
    print("-- END OF WISHLIST --")

    # show navigation options (main menu or exit)
    show_navigation()

def show_books_to_add(cursor, user_id):
    '''Function to show books not currently in user's wishlist'''

    # display header
    print("\n-- BOOKS AVAILABLE TO ADD TO WISHLIST --\n")

    # SQL select query to get books NOT in user's wishlist
    cursor.execute("SELECT book_name, author, details, book_id FROM book" +
                    " WHERE book_id NOT IN (SELECT book_id FROM wishlist" +
                    " WHERE user_id = " + str(user_id) + ")" +
                    " ORDER BY book_name")
    
    books_to_add = cursor.fetchall()

    # print list of books not in user's wishlist
    for book in books_to_add:
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Details: {book[2]}")
        print(f"Book ID: {book[3]}\n")

    # end of list message
    print("-- END OF LIST --")

    # create list of book_ids from books_to_add list for validation purposes
    books_to_add_ids = []
    for book in books_to_add:
        books_to_add_ids.append(str(book[3]))

    # get info from user on book to be inserted
    book_id = input("\nEnter the Book ID of the book you want to add to your wishlist:\n(m to return to main menu)\n>> ")
         
    # while loop to ensure input book_id is valid   
    while book_id not in books_to_add_ids and book_id.lower() != "m":
        book_id = input("\nINVALID INPUT: Please enter a valid book_id\n(m to return to main menu)\n>> ")

    # allow exit to main menu
    if book_id.lower() == "m":
        show_menu()
    else:
        # if valid book_id, return it
        return book_id

def add_book_to_wishlist(cursor, user_id, book_id):
    '''Function to add a book to a user's wishlist'''

    # SQL insert into wishlist table
    cursor.execute("INSERT INTO wishlist (user_id, book_id)" +
                    "VALUES (" + user_id + ", " + book_id + ")")

    db.commit() # commit insert to database

    # get book_name from book_id added
    cursor.execute("SELECT book_name FROM book WHERE book_id = " + book_id)
    book_names = cursor.fetchall()
    
    for row in book_names:
        book_name = row[0]

    # print success statement with book_name
    print(f'\n"{book_name}" was successfully added to your wishlist.')
    
    # pause for 1 second on success message
    sleep(1)

    # show updated wishlist
    show_wishlist(cursor, user_id)

def show_navigation():
    '''Function to show main menu and exit options for easy navigation'''

    # display menu options
    print("\n  1. Main Menu\n  2. Exit Program")

    # prompt for user input
    user_selection = input("\n>> ")
    
    # while loop to ensure a valid menu option is selected
    while user_selection not in ("1", "2"):
        user_selection = input("\nINVALID INPUT: Please enter 1 or 2\n>> ")
    
    # navigate according to user selection
    if user_selection == "1":
        show_menu()
    if user_selection == "2":
        print("\n   Program terminated. Goodbye.")
        exit()


''' PROGRAM EXECUTION '''

try:
    # connect to whatabook database
    db = mysql.connector.connect(**config)

    # get the cursor object
    cursor = db.cursor()
    
    # main execution of program - starts by displaying main menu
    show_menu()

except mysql.connector.Error as err:
    # handle errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # close database connection

    db.close()