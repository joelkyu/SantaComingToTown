from flask_sqlalchemy import SQLAlchemy
from config import app


db = SQLAlchemy(app)
class Person(db.Model):
    # Unqiue Twitter handle, can be expanded into a list / for other platforms
    # like Instagram or Facebook.
    id = db.Column(db.Integer, primary_key=True)
    twitter = db.Column(db.String(50), unique=True)
    instagram = db.Column(db.String(50), unique=True)
    facebook = db.Column(db.String(50), unique=True)
    lower_price = db.Column(db.Float(precision=2), nullable=True)
    upper_price = db.Column(db.Float(precision=2), nullable=False)


class Characteristic(db.Model):
    """
    Represents one characteristic that the targeted person is attracted to /
    or not attracted to.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    alpha = db.Column(db.Float)
    beta = db.Column(db.Float)
