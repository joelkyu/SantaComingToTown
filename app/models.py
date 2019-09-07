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

    def load_user_sentiment(self):
        self.tweets = tweet.recentTweets(self.twitter)
        self.keywords = []
        for tweet in self.tweets:
            keywords.append(senti.extract_positives(senti.senti_analysis(tweet)))
        self.kv = senti.caculate_keyword_vector(self.tweets, self.keywords)

    def compatibility(self, compare_title, compare_price):
        count = 0
        strength_sum = []
        for keyword in range(len(self.keywords)):
            if self.keywords[keyword] in compare_title:
                count += 1
                strength_sum.append(senti.price_weighting(self.kv[keyword], compare_price,
                self.lower_price, self.upper_price))
        if len(strength_sum) == 0:
            return 0
        return sum(strength_sum) / len(strength_sum)


class Characteristic(db.Model):
    """
    Represents one characteristic that the targeted person is attracted to /
    or not attracted to.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    alpha = db.Column(db.Float)
    beta = db.Column(db.Float)
