import numpy
import re
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import operator

# remove stop words and characters in each words and contruct an array
ps = PorterStemmer()

# remove stop words and stemmed


def word_extraction(tweet):
    stop_words = stopwords.words('english')
    ignore = stop_words
    words = re.sub("[^\w]", " ",  tweet).split()
    # stem
    cleaned_text = [ps.stem(w.lower()) for w in words if w not in ignore]
    # remove_link = re.sub(
    #     r'^https?:\/\/.*[\r\n]*', '', cleaned_text, flags=re.MULTILINE)
    return cleaned_text

# create an array of words in all tweets and remove duplicates


def tokenize(tweets):
    words = []
    for tweet in tweets:
        w = word_extraction(tweet)
        words.extend(w)

    words = sorted(list(set(words)))
    return words


def getWordsDictionary(all_tweets):
    wordfreq = {}
    for tweet in all_tweets:
        for raw_word in tweet.split():
            word = raw_word.strip(string.punctuation)
            if word not in wordfreq:
                wordfreq[word] = 0
            wordfreq[word] += 1
    sorted_wordfreq = sorted(
        wordfreq.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_wordfreq


def generate_bag_of_words(all_tweets):
    vocab = tokenize(all_tweets)
    bag_vector = numpy.zeros(len(vocab))

    for tweet in all_tweets:
        words = word_extraction(tweet)
        bag_vector = numpy.zeros(len(vocab))
        for w in words:
            for i, word in enumerate(vocab):
                if word == w:
                    bag_vector[i] += 1

        print("{0}\n{1}\n".format(words, numpy.array(bag_vector)))
        # return bag_vector

    # a = numpy.arange(len(vocab) * len(all_tweets)
    #                  ).reshape(len(all_tweets), len(vocab))
    # print(bag_vector.sum(axis=0))
    return bag_vector
