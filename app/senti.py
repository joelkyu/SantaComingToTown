# Imports the Google Cloud client library
from google.cloud import language
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
        encoding_type='UTF32',
    )
    return sentiment.entities


def extract_positives(dict, alpha):
    """
    Takes in API result from the sentimental analysis, spits out COMMON nouns
    that have a positive significance above a certain `alpha`.
    """
    words = []
    for entry in dict[:len(dict)-1]:
        if entry['mentions']['sentiment']['score'] > alpha and
           entry['mentions']['type'] == 'COMMON':
           words.append(entry['name'])
    return words
    

if __name__ == '__main__':
    print(senti_analysis('Mom said jogging wasn\'t very fun!'))
