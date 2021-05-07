/*
Katie Klein
CSD 310
29 April 2021
Assignment 10.3 - WhatABook Database and Table Creation
*/

-- Drop user if exists
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- Create user
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Grant user privileges
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

-- Delete constraints
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;

-- Delete tables if exists
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS wishlist;


/* TABLE CREATION */

-- Create store table
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- Create book table
CREATE TABLE book (
    book_id     INT             NOT NULL   AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

-- Create user table
CREATE TABLE user (
    user_id     INT             NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);

-- Create wishlist table
CREATE TABLE wishlist (
    wishlist_id     INT     NOT NULL    AUTO_INCREMENT,
    user_id         INT     NOT NULL,
    book_id         INT     NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id)
);


/* INSERT STATEMENTS */

-- Insert 1 store record
INSERT INTO store(locale) VALUES('1800 Literary Lane, Bookstown, NE 68100');


-- Insert 9 book records

INSERT INTO book(book_name, author) VALUES('Mindful Running', 'Mackenzie L. Havey');

INSERT INTO book(book_name, author) VALUES('Pretty as a Picture', 'Elizabeth Little');

INSERT INTO book(book_name, author) VALUES('The Woman in Cabin 10', 'Ruth Ware');

INSERT INTO book(book_name, author) VALUES('The Kobold Guide to Board Game Design', 'Mike Selinker');

INSERT INTO book(book_name, author) VALUES('Where the Crawdads Sing', 'Delia Owens');

INSERT INTO book(book_name, author) VALUES('Britt-Marie Was Here', 'Fredrik Backman');

INSERT INTO book(book_name, author, details) VALUES('The Food Lab', 'J. Kenji Lopez-Alt', 'Better home cooking through science');

INSERT INTO book(book_name, author, details) VALUES('Point Blank', 'Anthony Horowitz', 'Book 2 in the Alex Rider series');

INSERT INTO book(book_name, author) VALUES('Beauty Queens', 'Libba Bray');


-- Insert 3 user records
INSERT INTO user(first_name, last_name) VALUES ('Harry', 'Potter');
INSERT INTO user(first_name, last_name) VALUES ('Hermione', 'Granger');
INSERT INTO user(first_name, last_name) VALUES ('Ron', 'Weasley');


-- Insert 3 wishlist records (1 per user)
INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE first_name = 'Harry'),
    (SELECT book_id FROM book WHERE book_name = 'The Woman in Cabin 10')
);

INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE first_name = 'Hermione'),
    (SELECT book_id FROM book WHERE book_name = 'Where the Crawdads Sing')
);

INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE first_name = 'Ron'),
    (SELECT book_id FROM book WHERE book_name = 'The Food Lab')
);