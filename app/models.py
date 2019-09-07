from flask_sqlalchemy import SQLAlchemy
from config import app
import tweet
import senti


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

    def get_user_twitter_feed(self):
        pass

    def compatibility(self, compare_title, compare_price):
        pass



class Characteristic(db.Model):
    """
    Represents one characteristic that the targeted person is attracted to /
    or not attracted to.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    alpha = db.Column(db.Float)
    beta = db.Column(db.Float)
