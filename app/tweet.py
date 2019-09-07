import tweepy

auth = tweepy.OAuthHandler('rkEzbstvgQ2MpBYXdV5jgSqNx', 'WE2IC8CYvHlsqJ9PmMDa9WhiHe6YnxUW3zqQLarlaLVy5DZSUp')

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)