- Clone the project
- First you need to install library such as NLTK, Tweepy, Sckitlearn
- The program will start by storing all the preprocessed data from 'pre_processed_data.txt' to array so we can use it for about analytics.
- In this project there are txt files such as cosine_results_100_0.3 which means the result over 100 tweets which threshold over 0.3
- In main I have imported function create_frequency_dict(tweets) which accepts list of tweets and return list of dictionary contains the frequency
- To test similarity function import cosineSimilarity(dict1, dict2) from similarity.py and insert 2 tweets.
- For the main program that I have right now you can tweak around the doc_len which parameter and cosine similarity threshold to test different results.
