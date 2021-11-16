#!/usr/bin/python
import sqlite3


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()

        # TODO: convert date to datetime

        conn.execute('''
            CREATE TABLE books (
                id INTEGER PRIMARY KEY NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                published_date TEXT NOT NULL 
            );
        ''')

        conn.commit()
        print("Books table created successfully")
    except:
        print("Books table creation failed - Maybe table")
    finally:
        conn.close()


def insert_book(book):
    inserted_book = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (author, title, published_date) VALUES (?, ?, ?)", (book['author'],
                    book['title'], book['published_date']))
        conn.commit()
        inserted_book = get_book_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_book


def get_books():
    books = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            book = {}
            book["id"] = i["id"]
            book["author"] = i["author"]
            book["title"] = i["title"]
            book["published_date"] = i["published_date"]
            books.append(book)

    except:
        books = []

    return books


def get_book_by_id(id):
    book = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE id = ?",
                       (id,))
        row = cur.fetchone()

        # convert row object to dictionary
        book["id"] = row["id"]
        book["author"] = row["author"]
        book["title"] = row["title"]
        book["published_date"] = row["published_date"]
    except:
        book = {}
    return book


def update_book(book):
    updated_book = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE books SET author = ?, title = ?, published_date = ? WHERE id =?",
                     (book["author"], book["title"], book["published_date"],
                     book["id"],))
        conn.commit()
        #return the book
        updated_book = get_book_by_id(book["id"])

    except:
        conn.rollback()
        updated_book = {}
    finally:
        conn.close()

    return updated_book


def delete_book(id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from books WHERE id = ?",
                      (id,))
        conn.commit()
        message["status"] = "Book deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete book"
    finally:
        conn.close()

    return message

