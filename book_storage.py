#!/usr/bin/python
"""
In this module we create a database connection and define functions
for working with data in it
"""
import sqlite3
import logging


def connect_to_db(name="database.db"):
    """
    Connecting to the database
    :return: connection
    """
    conn = sqlite3.connect(name)
    return conn


def create_db_table():
    """
    Creating table for storing books data
    :return:
    """
    try:
        conn = connect_to_db()

        # TODO: convert date to datetime

        conn.execute(
            """
            CREATE TABLE books (
                id INTEGER PRIMARY KEY NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                published_date TEXT NOT NULL 
            );
        """
        )

        conn.commit()
        logging.info("Books table created successfully")
    except Exception:
        logging.error("Books table creation failed")
    finally:
        conn.close()


def insert_book(book, db="database.db"):
    """
    Inserting new book to the database
    :param book: dict
    :return: inserted book
    """
    inserted_book = {}
    try:
        conn = connect_to_db(db)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO books (author, title, published_date) VALUES (?, ?, ?)",
            (book["author"], book["title"], book["published_date"]),
        )
        conn.commit()
        inserted_book = get_book_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_book


def get_books(db="database.db"):
    """
    Get list of all books stored in the database
    :return: list of books
    """
    try:
        conn = connect_to_db(db)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()

        # convert row objects to dictionary

        books = [convert_to_dict(book) for book in rows]

    except Exception:
        books = []

    return books


def get_book_by_id(id, db="database.db"):
    """
    Get book by id from the database
    :param id: int
    :return: book
    """
    try:
        conn = connect_to_db(db)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE id = ?", (id,))
        row = cur.fetchone()

        # convert row object to dictionary
        book = convert_to_dict(row)
    except Exception:
        book = {}
    return book


def update_book(book, db="database.db"):
    """
    Updating existing book data
    :param book: dict
    :return: updated book data
    """
    try:
        conn = connect_to_db(db)
        cur = conn.cursor()
        cur.execute(
            "UPDATE books SET author = ?, title = ?, published_date = ? WHERE id =?",
            (
                book["author"],
                book["title"],
                book["published_date"],
                book["id"],
            ),
        )
        conn.commit()
        # return the book
        updated_book = get_book_by_id(book["id"])

    except Exception:
        conn.rollback()
        updated_book = {}
    finally:
        conn.close()

    return updated_book


def delete_book(id, db="database.db"):
    """
    Deleting book by id
    :param id: int
    :return: status message
    """
    message = {}
    try:
        conn = connect_to_db(db)
        conn.execute("DELETE from books WHERE id = ?", (id,))
        conn.commit()
        message["status"] = "Book deleted successfully"
    except Exception:
        conn.rollback()
        message["status"] = "Cannot delete book"
    finally:
        conn.close()

    return message


def convert_to_dict(row):
    """
    Converting row data to book dict
    :param row: row from DB query
    :return:
    """
    return {
        "id": row["id"],
        "author": row["author"],
        "title": row["title"],
        "published_date": row["published_date"],
    }
