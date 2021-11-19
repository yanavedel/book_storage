# book_storage
RESTful Python service to manage book storage. Using SQLite3 as a database and Flask to build the service.
To run the service run


`pip install -r requirements.txt`

`python app.py`


### Show all books
Returns json data about a single user.

- URL

    /api/books

- Method:

    GET

- URL Params

    None

- Data Params

    None

- Success Response:

    Code: 200

    Content: `[
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    },
    {
        "author": "Lisa Unger",
        "id": 2,
        "published_date": "01-04-2021",
        "title": "Ink and Bone"
    }]`

### Show book by id
Returns json data about a single user.

- URL

    /api/books/:id

- Method:

    GET

- URL Params

    id=[integer]

- Data Params

    None

- Success Response:

    Code: 200

    Content: `
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    }`
    
### Update book by id
Returns json data about a single user.

- URL

    /api/books/update

- Method:

    PUT

- URL Params

    None

- Data Params

    `
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    }`

- Success Response:

    Code: 200

    Content: `
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    }`

### Add book
Returns json data about a single user.

- URL

    /api/books/add

- Method:

    POST

- URL Params

    None

- Data Params

    `
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    }`

- Success Response:

    Code: 200

    Content: `
    {
        "author": "Lisa Unger",
        "id": 1,
        "published_date": "01-01-2020",
        "title": "Confessions on the 7:45"
    }`
    
 ### Delete book
Returns json data about a single user.

- URL

    /api/books/delete/:id

- Method:

    DELETE

- URL Params

    None

- Data Params

    None

- Success Response:

    Code: 200

    Content: `
    {
    "status": "Book deleted successfully"
}`