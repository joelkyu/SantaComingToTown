from flask_sqlalchemy import SQLAlchemy
from config import app
import tweet as tt
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
    # date until event

    def load_user_sentiment(self):
        self.tweets = tt.recentTweets(self.twitter)
        self.keywords = []
        for tweet in self.tweets:
            self.keywords.append(senti.extract_positives(senti.senti_analysis(tweet)))
        self.kv = senti.caculate_keyword_vector(self.tweets, self.keywords[0])


    def compatibility(self, compare_title, compare_price):
        self.load_user_sentiment()
        strength_sum = []
        for i in range(len(self.keywords[0])):
            if self.keywords[0][i][0].lower() in compare_title.lower():
                strength_sum.append(senti.price_weighting(list(self.kv[i].values())[0], compare_price,
                self.lower_price, self.upper_price))
        if len(strength_sum) == 0:
            return 0
        print(strength_sum)
        return sum(strength_sum) / len(strength_sum)

    def deserialize(self):
        self.load_user_sentiment()
        return {
            "id": self.id,
            "twitter": self.twitter,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "lower_price": self.lower_price,
            "upper_price": self.upper_price,
            "keywords": self.keywords,
            "tweets": self.tweets,
            "keyword-vector": self.kv,
        }

    def __repr__(self):
        return f'<{self.twitter}>'


class Characteristic(db.Model):
    """
    Represents one characteristic that the targeted person is attracted to /
    or not attracted to.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    alpha = db.Column(db.Float)
    beta = db.Column(db.Float)
