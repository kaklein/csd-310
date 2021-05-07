# Katie Klein
# CSD 310
# WhatABook
# 7 May 2021

'''
This program allows WhatABook customers to view their catalog,
view their store locations, and access a personal account
wherein users can view and add to their wishlist.

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


''' CONNECTING TO WHATABOOK SQL DATABASE '''

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

    # display header, instructions, and menu options
    print("\n-- MAIN MENU --")
    print("Enter a number to select one of the following options:")
    print("\n  1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit Program")
    
    # get selection from user
    main_selection = int(input("\n>> "))

    # if View Books is chosen
    if main_selection == 1:
        show_books(cursor)

    # if View Store Locations is chosen
    if main_selection == 2:
        show_locations(cursor)

    # if My Account is chosen
    if main_selection == 3:
        user_id = validate_user(cursor)
        show_account_menu(cursor, user_id)

    # if Exit Program is chosen
    if main_selection == 4:
        exit()

def show_books(cursor):
    '''Function to show all books in WhatABook catalog'''

    # print header
    print("\n-- BOOK CATALOG --\n")
    
    # SQL query to show contents from book table
    cursor.execute('SELECT book_name, author, details, book_id FROM book ORDER BY book_name')
    books = cursor.fetchall()
    for book in books:
        print(f"Title: {book[0]}\nAuthor: {book[1]}\nDetails: {book[2]}\nBook ID: {book[3]}\n")

    # end of catalog message
    print("-- END OF CATALOG --")

    # show navigation options (main menu or exit)
    show_navigation()

def show_locations(cursor):
    '''Function to show all WhatABook store locations'''

    # print header
    print("\n-- WHATABOOK STORE LOCATIONS --\n")

    # SQL query to show contents from store table
    cursor.execute('SELECT * FROM store')
    stores = cursor.fetchall()
    for store in stores:
        print(f"Address: {store[1]}")
        print(f"Store ID: {store[0]}\n")

    # end of list message
    print("-- END OF STORE LIST --")

    # show navigation options (main menu or exit)
    show_navigation()

def validate_user(cursor):
    '''Function to validate user_id against user table in database'''

    # display header
    print("\n-- ACCOUNT LOGIN --\n")

    # SQL query to get list of all user_ids
    cursor.execute('SELECT user_id FROM user')
    user_id_list = []
    query_results = cursor.fetchall()
    for row in query_results:
        user_id_list.append(row[0])

    # prompt for user_id
    user_id = int(input("Enter your user_id number: "))
    while (user_id not in user_id_list): # compare user_id to list all user_ids in database
        user_id = int(input("Invalid user_id. Please enter a valid user_id number: "))

    # display success message
    print("\nThank you, user_id accepted.\n")

    # pause before displaying account information
    sleep(1)

    # return user_id for use in account menu
    return user_id

def show_account_menu(cursor, user_id):
    '''Function to show account menu options and allow selection'''

    # get name of user
    query = 'SELECT first_name FROM user WHERE user_id = ' + str(user_id)
    cursor.execute(query)
    first_name = cursor.fetchall()
    
    # print account header with name
    for name in first_name:
        print(f"-- {name[0].upper()}'S ACCOUNT --")

    # show account menu
    print("  1. View Wishlist\n  2. Add Book\n  3. Main Menu")

    # store user input
    account_selection = int(input("\n>> "))
    
    # if View Wishlist is selected
    if account_selection == 1:
        show_wishlist(cursor, user_id)
    # if Add Book is selected
    if account_selection == 2:
        book_id = show_books_to_add(cursor, user_id)
        add_book_to_wishlist(cursor, user_id, book_id)
    # if Main Menu is selected
    if account_selection == 3:
        show_menu()

def get_user_wishlist(user_id):
    '''Function to store SQL select statement for a specific user's wishlist based on user_id'''

    # inner query gets info for ALL items in wishlist table
    inner_query = 'SELECT book_name, author, details, book.book_id AS book_id, wishlist.user_id AS user_id FROM book INNER JOIN wishlist ON wishlist.book_id = book.book_id'
    # outer query gets info for items on specific user's wishlist
    user_wishlist_select = 'SELECT book_name, author, details, book_id FROM (' + inner_query + ') AS consolidated_wishlist WHERE consolidated_wishlist.user_id = ' + str(user_id)
    
    return user_wishlist_select

def show_wishlist(cursor, user_id):
    '''Function to show a specific user's wishlist'''

    # display header
    print("\n-- WISHLIST --\n")
    
    # get user's wishlist
    user_wishlist_select = get_user_wishlist(user_id) # call function to get select query with specific user_id
    cursor.execute(user_wishlist_select) # execute select query
    user_wishlist = cursor.fetchall()
    
    # print user's wishlist
    for row in user_wishlist:
        print(f"Title: {row[0]}")
        print(f"Author: {row[1]}")
        print(f"Details: {row[2]}")
        print(f"Book ID: {row[3]}\n")

    # print end of list message
    print("-- END OF WISHLIST --")

    # show navigation options (main menu or exit)
    show_navigation()

def show_books_to_add(cursor, user_id):
    '''Function to show books not currently in user's wishlist'''

    # display header
    print("\n-- BOOKS AVAILABLE TO ADD TO WISHLIST --\n")

    # get user's wishlist
    user_wishlist = get_user_wishlist(user_id)

    # SQL select query to get books NOT in user's wishlist
    # all_books_query gets book_name, author, and user_id for all items in wishlist table
    all_books_query = 'SELECT book_name, author, details, book_id FROM book ORDER BY book_name'
    # outer query gets list of books not already in user's wishlist
    outer_query = ("SELECT book_name, author, details, book_id FROM (" + all_books_query + ") "
    "AS all_books WHERE book_id NOT IN (SELECT user_wishlist.book_id "
    "FROM (" + user_wishlist + ") AS user_wishlist)"
    )
    
    cursor.execute(outer_query)

    books_to_add = cursor.fetchall()
    for book in books_to_add:
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Details: {book[2]}")
        print(f"Book ID: {book[3]}\n")

    # end of list message
    print("-- END OF LIST --")

    # get info from user on book to be inserted
    book_id = input("\nEnter the Book ID of the book you want to add to your wishlist:\n>> ")

    return book_id

def add_book_to_wishlist(cursor, user_id, book_id):
    '''Function to add a book to a user's wishlist'''

    # SQL insert into wishlist table
    cursor.execute("INSERT INTO wishlist (user_id, book_id)"
    "VALUES (" + str(user_id) + ", " + str(book_id) + ")")

    # get book_name from book_id added
    cursor.execute('SELECT book_name FROM book WHERE book_id = ' + book_id)
    book_names = cursor.fetchall()
    
    for row in book_names:
        book_name = row[0]

    # print success statement
    print(f'\n"{book_name}" was successfully added to your wishlist.')
    sleep(1)

    # show updated wishlist
    show_wishlist(cursor, user_id)

def show_navigation():
    '''Function to show main menu and exit options for easy navigation'''

    # display menu options
    print("\n  1. Main Menu\n  2. Exit Program")

    # allow user input and navigate accordingly
    user_selection = int(input("\n>> "))
    if user_selection == 1:
        show_menu()
    if user_selection == 2:
        exit()

''' PROGRAM EXECUTION '''
# call main function
try:
    # connect to whatabook database
    db = mysql.connector.connect(**config)

    # get the cursor object
    cursor = db.cursor()
    
    # execute program - starts by displaying main menu
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