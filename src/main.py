import tweepy
from pprint import pprint
from twitter import get_credential

credential = get_credential()
auth = tweepy.OAuthHandler(
    credential['CONSUMER_KEY'], credential['CONSUMER_SECRET'])
auth.set_access_token(credential['ACCESS_TOKEN'],
                      credential['ACCESS_SECRET'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.get_user('twitter')
search_results = api.search(q="*", count=100, tweet_mode='extended')

for i in search_results:
    pprint(i)
    print('\n\n\n')

    # print(user.screen_name)
    # print(user.followers_count)
    # for friend in user.friends():
    #     print(friend.screen_name)
    # for tweet in public_tweets:
    #     pprint(tweet.text)
    #     print('\n')
    # print(public_tweets.length)
