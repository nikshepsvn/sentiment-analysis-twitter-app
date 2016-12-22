import tweepy
from textblob import TextBlob

ckey = 'lcpwIoF1afnBCMjW0U94jC7nr'
csecret ='kbbEcLjs1dSPTPqL37H56PyufF0cfcy7kMxYAcMs9ADe29zBzf'

atoken='3500178979-KRsq2qde9Y9qRq1Ja8LXFSzCjyLYVVxEGa9aMxi'
asecrettoken='paMPDmbVQRrLXPo8mtiSMWgDyMGvDSYljKZBYqK2TgCGW'

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecrettoken)

api = tweepy.API(auth)

print ("twitter sentiment analysis bot running...")
searchword=input("please enter search world to find sentiments for..")

tweets = api.search(searchword)

for tweet in tweepy.Cursor(api.search,
                           q="google",
                           count=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
  


