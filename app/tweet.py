import tweepy

auth = tweepy.OAuthHandler('rkEzbstvgQ2MpBYXdV5jgSqNx', 'WE2IC8CYvHlsqJ9PmMDa9WhiHe6YnxUW3zqQLarlaLVy5DZSUp')

api = tweepy.API(auth)

def recentTweets(username):
    return [tweet.text for tweet in tweepy.Cursor(api.search, q=username).items(20)]


