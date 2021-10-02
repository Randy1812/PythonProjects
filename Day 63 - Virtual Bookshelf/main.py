# from flask import Flask, render_template,request
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
#
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# # Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#     # Optional: this will allow each book object to be identified by its title when printed.
#     def __repr__(self):
#         return f'<Book {self.title}>'
#
#
# db.create_all()
#
#
# all_books = []
#
#
# # db = sqlite3.connect("books-collection.db")
# # cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
# #                "NOT NULL, rating FLOAT NOT NULL)")
#
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', 9.5)")
# # cursor.execute("INSERT INTO books VALUES(2, 'Tale of Two Cities', 'Charles Dickens', 7.0)")
# # db.commit()
#
#
# @app.route('/')
# def home():
#     if request.method == "POST":
#         # book = {
#         #     "title": request.form["bk_title"],
#         #     "author": request.form["bk_author"],
#         #     "rating": request.form["bk_rating"]
#         # }
#         # all_books.append(book)
#         # print(all_books)
#         new_book = Book(title=request.form["bk_title"], author=request.form["bk_author"], rating=request.form["bk_rating"])
#         db.session.add(new_book)
#         db.session.commit()
#     else:
#         all_books = db.session.query(Book).all
#         for book in all_books:
#             print(book["title"])
#     # return render_template("index.html", books=all_books)
#     return render_template("index.html")
#
#
# @app.route("/add", methods=["GET", "POST"])
# def add():
#     return render_template("add.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


# ***** REDONE HERE ******#

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'],
                        author=request.form['author'],
                        rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<int:bookid>', methods=["GET", "POST"])
def edit(bookid):
    book = Book.query.get(bookid)
    if request.method == "POST":
        new_rating = request.form['rating']
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)


@app.route('/delete/<int:bookid>')
def delete(bookid):
    book = Book.query.get(bookid)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
