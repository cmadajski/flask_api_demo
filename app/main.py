from flask import Flask, jsonify, abort
from books import books

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	welcome = {
		"author": "Christian Madajski",
		"version": "v1.0",
		"methods_allowed": [
			"GET",
			"POST",
			"PUT",
			"DELETE"
		],
		"endpoints": {
			"/get_books": "gets all books available in the system",
			"/get_book/id": "gets a specific book by ID",
			"/add_book": "adds a new book to the system",
			"/change_book": "modifies an existing book's data",
			"/delete_book": "removes an existing book from the system"
		}
	}
	return jsonify(welcome)

@app.route('/books', methods=["GET"])
def get_books():
	return jsonify(books)

@app.route('/book/<int:id>', methods=['GET'])
def get_book(id):
	# check to see if 
	try:
		return jsonify(books[id])
	except KeyError:
		abort(404)
			
@app.route('/book', methods=['POST'])
def post_book():
	return "POST IS WORKING"

@app.route('/book/<int:id>', methods=['PUT'])
def modify_book(id):
	return "PUT IS WORKING"

@app.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
	try:
		del books[id]
		return jsonify({
			"id": id,
			"status": "deleted"
		})
	except KeyError:
		return jsonify({
			"status": "404",
			"error": "KeyError",
			"message": "ID value not valid"
		})

@app.errorhandler(404)
def not_found(e):
	return jsonify({
		"error": 404,
		"message": "The data requested cannot be found"
	})


if __name__ == "__main__":
	app.run(debug=True)
