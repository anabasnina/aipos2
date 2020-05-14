from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    genre = StringField('Genre')
    year_of_writing = StringField('Year of writing')
    pages = StringField('Pages')
    publish_house = StringField('Publish house')
    submit = SubmitField()


class AuthorForm(FlaskForm):
    name = StringField('Author', validators=[DataRequired()])
    direction = StringField('Direction')
    date_of_birth = StringField('Date of birth')
    submit = SubmitField()


class PublishHouseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address')
    phone_num = StringField('Phone number')
    website = StringField('Website')
    submit = SubmitField()
