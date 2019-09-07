# Imports the Google Cloud client library
from google.cloud import language
import json
from google.cloud.language import enums
from google.cloud.language import types


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
        encoding_type='UTF16',
    )
    return sentiment.entities


def extract_positives(dict, alpha, beta):
    """
    Takes in API result from the sentimental analysis, spits out COMMON nouns
    that have a positive significance above a certain `alpha`. The significance
    must also be greater than beta.
    """
    words = []
    for entry in range(len(dict) - 1):
        if dict[entry].sentiment.score > alpha and dict[entry].sentiment.magnitude > beta:
            if dict[entry].mentions.type == "COMMON":
                words.append(dict[entry].name)
    return words


if __name__ == '__main__':
    dict = senti_analysis('I hate jogging!')
    print(extract_positives(dict, alpha=-1, beta=0.1))
