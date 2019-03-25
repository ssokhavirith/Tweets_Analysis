import json


def get_credential():
    with open('src/api/twitter_credentials.json') as f:
        twitter_credential = json.load(f)
    return twitter_credential
