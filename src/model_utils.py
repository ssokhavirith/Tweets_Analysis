from nltk.stem import PorterStemmer, WordNetLemmatizer
from utils import tokenize
import re

lemma = WordNetLemmatizer()
ps = PorterStemmer()


def count_words(words):
    count = 0
    words = len(words.split(" "))
    for word in words:
        count += 1
    return count


def create_frequency_dict(tweets):
    i = 0
    freqDict_list = []
    for tweet in tweets:
        i += 1
        freq_dict = {}
        words = tweet.split()
        for word in words:
            # if word already existsin dict increment
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id': i, 'freq_dict': freq_dict, 'tweet': tweet}
        freqDict_list.append(temp)
    return freqDict_list

# def computerTF(freqDict_list):
