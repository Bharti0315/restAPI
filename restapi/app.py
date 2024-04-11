from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')

# Sample data for books
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Development", "author": "Jane Smith"}
]

max_id = max(book['id'] for book in books)

@app.route('/index')
def index():
    return render_template ('index.html')

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by id
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    global max_id
    new_book = request.json
    max_id += 1  # Increment the maximum ID
    new_book['id'] = max_id  # Assign the new ID to the new book
    books.append(new_book)
    return jsonify(new_book), 201

# Update an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(request.json)
        return jsonify(book), 200
    else:
        return jsonify({"error": "Book not found"}), 404

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=8000)
