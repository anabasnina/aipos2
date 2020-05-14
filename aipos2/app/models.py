from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    year_of_writing = db.Column(db.String(255))
    pages = db.Column(db.String(255))
    publish_house_id = db.Column(db.Integer, db.ForeignKey('publish_houses.id'))

    def __repr__(self):
        return self.title


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    direction = db.Column(db.String(255))
    date_of_birth = db.Column(db.String(255))
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return self.name


class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', backref='genre')

    def __repr__(self):
        return self.genre


class PublishHouse(db.Model):
    __tablename__ = 'publish_houses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    phone_num = db.Column(db.String(20))
    website = db.Column(db.String(255))
    books = db.relationship('Book', backref='publish_house')

    def __repr__(self):
        return self.name
