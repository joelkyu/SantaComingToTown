# Imports the Google Cloud client library
import os
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


def extract_positives(dict, alpha, beta):
    """
    Takes in API result from the sentimental analysis, spits out COMMON nouns
    that have a positive significance above a certain `alpha`. The significance
    must also be greater than beta.
    """
    words = []
    for entry in range(len(dict)):
        print(dict[entry].mentions[0].type)
        print('________________\n')
        if dict[entry].sentiment.score > alpha and dict[entry].sentiment.magnitude > beta:
            if dict[entry].mentions[0].type == 2:
                words.append(dict[entry].name)
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


if __name__ == '__main__':
    print(extract_positives(senti_analysis('I love pizza so so so much.'), 0.5, 0.5))
    print(extract_adj("OMG THIS SWEATER IS SO FLUFFY."))
