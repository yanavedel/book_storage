from flask import Flask, request, jsonify
from flask_cors import CORS
from create_storage import get_books, get_book_by_id, insert_book, update_book, delete_book

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/books', methods=['GET'])
def api_get_books():
    return jsonify(get_books())


@app.route('/api/books/<book_id>', methods=['GET'])
def api_get_book(book_id):
    return jsonify(get_book_by_id(book_id))


@app.route('/api/books/add',  methods = ['POST'])
def api_add_book():
    book = request.get_json()
    return jsonify(insert_book(book))


@app.route('/api/books/update',  methods = ['PUT'])
def api_update_book():
    book = request.get_json()
    return jsonify(update_book(book))


@app.route('/api/books/delete/<book_id>',  methods = ['DELETE'])
def api_delete_book(book_id):
    return jsonify(delete_book(book_id))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()
