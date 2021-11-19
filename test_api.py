import flask_unittest

from flask import Flask

from app import *
from book_storage import *


class TestApi(flask_unittest.ClientTestCase):
    app = Flask(__name__)

    def test_api_get_books(self, client):

        books = get_books()
        response = app.test_client().get("/api/books")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(books, response.json)

    def test_api_get_book_by_id(self, client):

        book = get_books()[-1]
        book_id = book["id"]
        response = app.test_client().get("/api/books/{}".format(book_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(book, response.json)

    def test_api_add_book(self, client):

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

    def test_api_update_book(self, client):

        books = get_books()
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

    def test_api_delete_book(self, client):
        book = get_books()[-1]
        book_id = book["id"]
        len_before = len(get_books())
        response = app.test_client().delete("/api/books/delete/{}".format(book_id))
        self.assertEqual(response.status_code, 200)
        self.assertLess(len(get_books()), len_before)
