# Imports the Google Cloud client library
import os
import math
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


# Set environmental variable to local OAuth2.0 file
os.putenv("GOOGLE_APPLICATION_CREDENTIALS", "auth.json")

# Instantiates a client
client = language.LanguageServiceClient()


def senti_analysis(text: str):
    """
    :param text: Plain text to be analyzed for sentimental analysis.
    :return: a list of entries with the last one being a summary for the
    salience value and sentimental value for the entire sentence.
    Evaluation for each word is as following:
        name: str
        type: str
        mentions: {
            text:  str
            type: noun type str
            sentiment {
                magnitude: [0, 1]
                score: [-1, 1]
            }
        }
    """
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )
    sentiment = client.analyze_entity_sentiment(
        document=document,
        encoding_type='UTF32',
    )
    # print(sentiment.entities)
    return sentiment.entities


def extract_positives(dict):
    """
    Takes in API result from the sentimental analysis, spits out COMMON nouns
    that have a positive significance above a certain `alpha`. The significance
    must also be greater than beta.
    """
    words = []
    for entry in range(len(dict)):
        words.append((dict[entry].name, dict[entry].sentiment.score, dict[entry].sentiment.magnitude))
        # α = sentiment score, β = sentiment magnitude
    # TODO: extract adjectives if the sentence is generally positive.
    # Sometimes it is the adjective that they are more attracted to compared
    # to the actual prodct.
    return words


def extract_adj(text):
    document = {
        "content": text,
        "type": 'PLAIN_TEXT',
        "language": 'en'
    }
    response = client.analyze_syntax(document, encoding_type='UTF32')
    adj = []
    for token in response.tokens:
        # print(type(token.part_of_speech))
        if enums.PartOfSpeech.Tag(token.part_of_speech.tag).name == "ADJ":
            adj.append(token.text.content)

    return adj


def extract_k(tweets, text):
    k = 0
    for tweet in tweets:
        if text in tweet.split(' '):
            k += 1
    return k


def caculate_keyword_vector(tweets, keywords):
    v = []
    for word in keywords[0]:
        k = extract_k(tweets, word[0])
        a = word[1]
        b = word[2]
        v.append(
            {
                word[0]: 0.5 * b * (a + 1) * ((math.exp(k) - 1) / (1 + math.exp(k)))
            }
        )
    return v


def price_weighting(s: float, price: float, p_min: float, p_max: float):
    u_diff = p_max - price
    l_diff = price - p_min
    if u_diff < 0:
        return 0 if s - 0.05(u_diff)**2 < 0 else s - 0.05(u_diff)**2
    elif l_diff < 0:
        return 0 if s - 0.05(l_diff)**2 < 0 else s - 0.05(l_diff)**2
    else:
        return s
