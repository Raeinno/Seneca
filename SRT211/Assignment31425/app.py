'''
Develop a web application that allows users to add new books to a database and view a list of all books. This project will help students understand and implement basic Create and Read operations within a web application framework using Flask and a MySQL database.
Project Specifications:

    Database Setup:

    Create a library database in MySQL.
    Establish a books table with fields for id, title, author, genre, and published_year.

    Flask Application:

    Configure the Flask app to connect to the MySQL database.
    Implement a route to display a form for adding new books.
    Implement a route to handle the submission of the form and insertion of book data into the database.
    Implement a route to retrieve and display all books from the database.

    Frontend:

    Create HTML forms for adding books to the database.
    Display a list of all books in a structured format, such as a table, which includes all the details of the books.
'''

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import MySQLdb

app = Flask(__name__)
app.debug = True

# Creating a mysql interface
mysql1 = MySQLdb.connect("localhost","root","13822831","library")
mysql = mysql1.cursor()


@app.route('/') #Main page.
def main_page():
    return render_template('index.html')

@app.route('/add_book',methods=['post']) #Option to add a new book goes to the add_book page.
def addask():
    return render_template('add_book.html')

@app.route('/new_book', methods = ['POST','GET'])
#Adding the user inputed values to the sql.
def add_book():
    book_detail = request.form
    title = book_detail['title']
    author = book_detail['author']
    genre = book_detail['genre']
    published_year = book_detail['published_year']
    mysql.execute("USE library;")
    mysql.execute("""INSERT INTO books (title, author, genre, published_year) values (""%s"",""%s"",""%s"",""%s"");""",(title,author,genre,published_year))
    mysql1.commit()
    return redirect('/')
    
@app.route('/view_books', methods = ['POST','GET'])
#View the table
def view_book():
    

    book = mysql.execute("select * from books;")
    if book > 0:
        booksql = mysql.fetchall()
    return render_template('view_book.html',sql1s=booksql)


if __name__ == '__main__':
    app.run()