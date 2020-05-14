from flask import render_template, request, redirect, url_for

from app import app
from .forms import BookForm, AuthorForm, PublishHouseForm
from .models import Book, Author, Genre, PublishHouse, db


@app.route('/')
def index():
    return render_template('navigation.html')


@app.route('/books/')
def books():
    books = db.session.query(Book).all()
    return render_template('books.html', books=books)


@app.route('/books/add/', methods=['get', 'post'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = update_book(form)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_edit_smth.html', title='Add book', form=form)


@app.route("/books/<int:book_id>/edit/", methods=['get', 'post'])
def edit_book(book_id):
    book = db.session.query(Book).filter(Book.id == book_id).one()
    form = BookForm()
    if form.validate_on_submit():
        update_book(form, book)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    else:
        form.title.data = book.title
        form.author.data = book.author
        form.genre.data = book.genre
        form.year_of_writing.data = book.year_of_writing
        form.pages.data = book.pages
        form.publish_house.data = book.publish_house
        return render_template('add_edit_smth.html', title='Edit book', form=form)


@app.route('/books/<int:book_id>/delete/', methods=['get', 'post'])
def delete_book(book_id):
    book = db.session.query(Book).filter(Book.id == book_id).one()
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('books'))
    else:
        return render_template('delete_smth.html', title='Delete book', smth=book)


@app.route('/authors/')
def show_authors():
    authors = db.session.query(Author).all()
    return render_template('authors.html', authors=authors)


@app.route('/authors/add/', methods=['get', 'post'])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        author = update_author(form)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    return render_template('add_edit_smth.html', title='Add author', form=form)


@app.route('/authors/<int:author_id>/edit/', methods=['get', 'post'])
def edit_author(author_id):
    author = db.session.query(Author).filter(Author.id == author_id).one()
    form = AuthorForm()
    if form.validate_on_submit():
        update_author(form, author)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    else:
        form.name.data = author.name
        form.direction.data = author.direction
        form.date_of_birth.data = author.date_of_birth
        return render_template('add_edit_smth.html', title='Edit author', form=form)


@app.route('/authors/<int:author_id>/delete/', methods=['get', 'post'])
def delete_author(author_id):
    author = db.session.query(Author).filter(Author.id == author_id).one()
    if request.method == 'POST':
        db.session.delete(author)
        db.session.commit()
        return redirect(url_for('show_authors'))
    else:
        return render_template('delete_smth.html', title='Delete author', smth=author)


@app.route('/publishers/')
def show_publishers():
    publishers = db.session.query(PublishHouse).all()
    return render_template('publishers.html', publishers=publishers)


@app.route('/publishers/add', methods=['get', 'post'])
def add_publisher():
    form = PublishHouseForm()
    if form.validate_on_submit():
        publisher = update_publisher(form)
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for('show_publishers'))
    return render_template('add_edit_smth.html', title='Add publish house', form=form)


@app.route('/publishers/<int:publisher_id>/edit', methods=['get', 'post'])
def edit_publisher(publisher_id):
    publisher = db.session.query(PublishHouse).filter(PublishHouse.id == publisher_id).one()
    form = PublishHouseForm()
    if form.validate_on_submit():
        update_publisher(form, publisher)
        db.session.add(publisher)
        db.session.commit()
        return redirect(url_for('show_publishers'))
    else:
        form.name.data = publisher.name
        form.address.data = publisher.address
        form.phone_num.data = publisher.phone_num
        form.website.data = publisher.website
        return render_template('add_edit_smth.html', title='Edit publish house', form=form)


@app.route('/publishers/<int:publisher_id>/delete', methods=['get', 'post'])
def delete_publisher(publisher_id):
    publisher = db.session.query(PublishHouse).filter(PublishHouse.id == publisher_id).one()
    if request.method == 'POST':
        db.session.delete(publisher)
        db.session.commit()
        return redirect(url_for('show_publishers'))
    else:
        return render_template('delete_smth.html', title='Delete publish house', smth=publisher)


@app.route('/genres/')
def show_genres():
    genres = db.session.query(Genre).all()
    return render_template('genres.html', genres=genres)


@app.route('/genres/<int:genre_id>/delete', methods=['get', 'post'])
def delete_genre(genre_id):
    genre = db.session.query(Genre).filter(Genre.id == genre_id).one()
    if request.method == 'POST':
        db.session.delete(genre)
        db.session.commit()
        return redirect(url_for('show_genres'))
    else:
        return render_template('delete_smth.html', title='Delete genre', smth=genre)


def update_book(form, book=None):
    title = form.title.data
    author_name = form.author.data
    genre_name = form.genre.data if form.genre.data != '' else None
    year = form.year_of_writing.data if form.year_of_writing.data != '' else None
    pages = form.pages.data if form.pages.data != '' else None
    publish_house_name = form.publish_house.data if form.publish_house.data != '' else None

    if book is None:
        book = Book()

    book.title = title
    book.year_of_writing = year
    book.pages = pages

    query_res = db.session.query(Author).filter(Author.name == author_name).first()
    if query_res is None:
        author = Author(name=author_name)
    else:
        author = query_res
    book.author = author

    if genre_name is not None:
        query_res = db.session.query(Genre).filter(Genre.genre == genre_name).first()
        if query_res is None:
            genre = Genre(genre=genre_name)
        else:
            genre = query_res
        book.genre = genre

    if publish_house_name is not None:
        query_res = db.session.query(PublishHouse).filter(PublishHouse.name == publish_house_name).first()
        if query_res is None:
            publish_house = PublishHouse(name=publish_house_name)
        else:
            publish_house = query_res
        book.publish_house = publish_house

    return book


def update_author(form, author=None):
    name = form.name.data
    direction = form.direction.data if form.direction.data != '' else None
    dom = form.date_of_birth.data if form.date_of_birth.data != '' else None

    if author is None:
        author = Author()

    author.name = name
    author.date_of_birth = dom
    author.direction = direction

    return author


def update_publisher(form, publisher=None):
    name = form.name.data
    address = form.address.data if form.address.data != '' else None
    phone_num = form.phone_num.data if form.phone_num.data != '' else None
    website = form.website.data if form.website.data != '' else None

    if publisher is None:
        publisher = PublishHouse()

    publisher.name = name
    publisher.address = address
    publisher.phone_num = phone_num
    publisher.website = website

    return publisher
