#Zach Thomas
#4/14/2024
#M04 Lab - Case Study: Python APIs
#    Note: I did most of the assignment in one sitting, but had to come back to it later. I am now receiving an error: "Import "flask_sqlalchemy" could not be resolvedPylance",
#    and haven't been able to fix it. 

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"


@app.route('/')
def index():
    return 'Hello'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {'books': 'book data'}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.name, 'author': book.author, 'publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'], )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {'error': 'not found'}
    db.sessions.delete(book)
    db.session.commit()
    return {'message': 'yeet!@'}

