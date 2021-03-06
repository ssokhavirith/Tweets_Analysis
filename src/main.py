import os
from nltk.corpus import stopwords
import string
import tweepy
from pprint import pprint
from twitter import get_credential
import nltk
import datetime
from utils import generate_bag_of_words, tokenize, word_extraction, getWordsDictionary
from model_utils import create_frequency_dict
from similarity import cosineSimilarity
from nltk.stem import PorterStemmer, WordNetLemmatizer

lemma = WordNetLemmatizer()

# ----- TWITTER API CONNECTION

# credential = get_credential()
# auth = tweepy.OAuthHandler(
#     credential['CONSUMER_KEY'], credential['CONSUMER_SECRET'])
# auth.set_access_token(credential['ACCESS_TOKEN'],
#                       credential['ACCESS_SECRET'])

# api = tweepy.API(auth, wait_on_rate_limit=True)
# user = api.get_user('twitter')

# user_ids = {
#     # "ElonMusk": 44196397,  # technology 1
#     # "BillGates": 50393960,  # tech 2
#     "SundarPichai": 14130366,  # tech google ceo 3
#     "TimCook": 1636590253,  # tech apple ceo 4
#     "JeffBezos": 15506669,  # amazon ceo 5
#     "EmilyChang": 74130577,  # influence women in tech industry 6
#     "MarquesBrownlee": 29873662,  # famous tech vlogger 7
#     "DavidHeinemeierHansson": 14561327,  # founder of ruby on rail 8
#     "ReshmaSaujani": 57172253,  # founder of girl who code 9
#     "KaraSwisher": 5763262,  # founder of ReCode(journalists) 10
#     "ChristopherMims": 1769191,  # journalists 11
#     "David Cohen": 817209,  # founder of Techstar 12
#     # "JeffWeiner": 20348377,  # ceo of linked in 13
#     "HuffPost": 73147282,  # news about technology 14
#     # A partner at the venture capital firm Andreessen Horowitz 15
#     "BenedictEvans": 1236101,
#     "BBCTech": 621583,  # 16
#     "ForbesTech": 14885549,  # 17
#     "AndrewNg": 216939636,  # 18
#     # Founder of machine intelligence research company Fast Forward Labs 19
#     "HilaryMason": 765548,
#     "SirajRaval": 2479063608,  # data scientist, talk about AI trends
# }

# # ------------------------

# # technology
# #
# file = open('tech_tweets_april2019.txt', 'a')
# startDate = datetime.datetime(2019, 4, 1, 0, 0, 0)
# endDate = datetime.datetime(2019, 5, 30, 0, 0, 0)

# for key, value in user_ids.iteritems():
#     tweets = tweepy.Cursor(api.user_timeline, user_id=value,
#                            include_rts=False, tweet_mode="extended").items()
#     idx = 0
#     for tweet in tweets:
#         if tweet.created_at <= endDate and tweet.created_at >= startDate and tweet.in_reply_to_user_id_str is None:
#             tweeted_by = key
#             created_date = tweet.created_at.strftime("%d %b")
#             tweet_id = tweet.id
#             tweet_text = tweet.full_text
#             tweet_text = str(tweet_text.encode('ascii', 'ignore').decode(
#                 'ascii').replace("\r\n", ""))
#             combinedString = tweeted_by + "--" + created_date + "--" + tweet_text
#             print(combinedString)
#             print('\n')
#             file.write(combinedString)
#             file.write('\n')
#             idx = idx + 1
# print("end of program")

# search_results = api.search(q="football -filter:retweets", count=100)
# game, football
# file = open('myfile.txt', 'a')
# f = open('tweets_data.txt', 'a')

# for index, tweet in enumerate(search_results):
#     tweet_text = tweet.text
#     tweet_id = tweet.id
#     tweet_text = str(tweet_text.encode('ascii', 'ignore').decode(
#         'ascii').replace("\r\n", ""))
#     pprint(str(tweet_id) + "--" + tweet_text)
#     f.write(str(tweet_id) + "--" + tweet_text)
#     f.write('\n')
# f.close()

# for tweet in search_results:
#     full_text = i['extended_tweet']['full_text']
#     text = i['text']
#     pprint(tweet['full_text'])
# if full_text:
#     file.append(full_text)
#     file.append('\n')
#     pprint(full_text)
#     pprint('\n')
# else:
#     file.append(text)
#     file.append('\n')
#     pprint(text)
#     pprint('\n')

# print(stopwords.words('english'))
# tweets = ["Joe waited for the train", "The train train train train train train was late late late", "Mary and Samantha took the bus",
#           "I looked for Mary and Samantha at the bus station",
#           "Mary and Samantha arrived at the bus station early but waited until noon for the bus"]

tweets = []
# pre_processed = open('pre_processed_data.txt', 'a')
# with open('tech_tweets_april2019.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         tweet = ' '.join(word_extraction(line.split("--")[2]))
#         pre_processed.write(tweet + '\n')
#         tweets.append(tweet)
# pre_processed.close()

with open('pre_processed_data.txt') as f:
    lines = f.readlines()
    for line in lines:
        tweets.append(line)
f.close()


# -------generate frequency document
frequency_dicts = create_frequency_dict(tweets)
doc_length = 100
cosine_similarity_threshold = 0.5
similarity_matrix = []


for freq_dict in frequency_dicts[:doc_length]:
    similarity_bag = [0] * doc_length
    count = 0
    for index, freq_dict_1 in enumerate(frequency_dicts[:doc_length]):
        freDict1 = freq_dict['freq_dict']
        freDict2 = freq_dict_1['freq_dict']
        cosine_sim_val = cosineSimilarity(freDict1, freDict2)
        if(cosine_sim_val > cosine_similarity_threshold):
            count += 1
            similarity_bag[index] = cosine_sim_val
        # if(cosine_sim_val)
    similarity_matrix.append(
        {'tweet': freq_dict['tweet'], 'total_similar_tweets': count, 'similarity_vector': similarity_bag})

cosine_similarity_results = open('cosine_results_100_0.5.txt', 'a')
highest_sim_tweet = similarity_matrix[0]
for row in similarity_matrix:
    if(row['total_similar_tweets'] > highest_sim_tweet['total_similar_tweets']):
        highest_sim_tweet = row
    cosine_similarity_results.write(
        row['tweet'] + ': ' + str(row['total_similar_tweets']) + '\n')
cosine_similarity_results.write('-----------------\n')
cosine_similarity_results.write(
    'Highest matches : ' + str(highest_sim_tweet['total_similar_tweets']) + '\n')
cosine_similarity_results.write('Tweet : ' + str(highest_sim_tweet['tweet']))

cosine_similarity_results.close()

# --------------------------------

# --------------------------- write frequency to file
# dict_words = getWordsDictionary(tweets)
# results = open('frequency_results.txt', 'a')
# for key, value in dict_words:
#     results.write(key + ' : ' + str(value) + '\n')
# results.close()
# ----------------------------
# print(getWordsDictionary(tweets))
# print(tokenize(tweets))
# bow_transformer = CountVectorizer
# extracted_tweets = []
# for tweet in tweets:
#     new_tweet = ' '.join(word_extraction(tweet))
#     extracted_tweets.append(new_tweet)

# print(getWordsDictionary(extracted_tweets))

# wordfreq = {}
# for raw_word in extracted_tweets[1].split():
#     word = raw_word.strip(string.punctuation)
#     if word not in wordfreq:
#         wordfreq[word] = 0
#     wordfreq[word] += 1
# print(wordfreq)
