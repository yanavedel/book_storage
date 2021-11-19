import flask_unittest
from mock import patch

from flask import Flask

from app import *
from book_storage import *


def connect_to_test_db():
    return connect_to_db(name="test_database.db")


class TestApi(flask_unittest.ClientTestCase):
    app = Flask(__name__)

    @patch('app.connect_to_db')
    def test_api_get_books(self, client, mock_connect_db):
        mock_connect_db.side_effect = connect_to_test_db
        books = get_books()
        response = app.test_client().get("/api/books")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(books, response.json)

    @patch('app.connect_to_db')
    def test_api_get_book_by_id(self, client, mock_connect_db):
        mock_connect_db.side_effect = connect_to_test_db
        book = get_books()[-1]
        book_id = book["id"]
        response = app.test_client().get("/api/books/{}".format(book_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(book, response.json)

    @patch('app.connect_to_db')
    def test_api_add_book(self, client, mock_connect_db):
        mock_connect_db.side_effect = connect_to_test_db
        response = app.test_client().post(
            "/api/books/add",
            json={
                "author": "New Author",
                "published_date": "15-08-2021",
                "title": "New Book",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_books()[-1], response.json)

    @patch('app.connect_to_db')
    def test_api_update_book(self, client, mock_connect_db):
        mock_connect_db.side_effect = connect_to_test_db
        response = app.test_client().put(
            "/api/books/update",
            json={
                "author": "New Author",
                "published_date": "15-08-2021",
                "title": "New New Book",
                "id": 1,
            },
        )
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(books, response.json)

    @patch('app.connect_to_db')
    def test_api_delete_book(self, client, mock_connect_db):
        mock_connect_db.side_effect = connect_to_test_db
        book = get_books()[-1]
        book_id = book["id"]
        len_before = len(get_books())
        response = app.test_client().delete("/api/books/delete/{}".format(book_id))
        self.assertEqual(response.status_code, 200)
        self.assertLess(len(get_books()), len_before)
        insert_book(book)
