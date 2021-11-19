"""
In this module we create requests for accessing and updating the book inventory
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from book_storage import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api/books", methods=["GET"])
def api_get_books():
    """
    Getting list of all stored books
    :return: list of books
    """
    return jsonify(get_books())


@app.route("/api/books/<book_id>", methods=["GET"])
def api_get_book(book_id):
    """
    Getting book data by id
    :param book_id: int
    :return: book: dict
    """
    return jsonify(get_book_by_id(book_id))


@app.route("/api/books/add", methods=["POST"])
def api_add_book():
    """
    Adding new book to the storage
    :return: inserted book
    """
    book = request.get_json()
    return jsonify(insert_book(book))


@app.route("/api/books/update", methods=["PUT"])
def api_update_book():
    """
    Updating existing book data by id
    :return:
    """
    book = request.get_json()
    return jsonify(update_book(book))


@app.route("/api/books/delete/<book_id>", methods=["DELETE"])
def api_delete_book(book_id):
    """
    Deleting book from the storage
    :param book_id: int
    :return: status message
    """
    return jsonify(delete_book(book_id))


if __name__ == "__main__":
    app.run(debug=True)
