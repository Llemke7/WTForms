from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, Optional

toolbar = DebugToolbarExtension()

db = SQLAlchemy()


def connect_db(app):
    """Connect DB"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'pet {self.name} {self.species}'

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional()])
    notes = TextAreaField('Notes')

class EditPetForm(FlaskForm):
    """Form to edit pets"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes')
    available = BooleanField('Available')