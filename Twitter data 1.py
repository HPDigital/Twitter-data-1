"""
Twitter data 1
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Enter Twitter API Keys
access_token = "551693427-9YxBcOd49wE6nKhNCeVX0RKURlc0rSPEMov9FoPR"
access_token_secret = "UtKnwyytjObFs3RRXhVrIwruljYUB6xbCkzJf4nbzMVZf"
consumer_key = "7GKwhJwazdDrgaXSzZvMrFGtT"
consumer_secret = "ceLNls49QUtprrLCTDsjaXRLQJ4hGhKcIQKf4p7sfiXVcljZJM"

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):

    def on_data(self, data):   
        print(data)
        return True


    def on_error(self, status):
        print(status)


if __name__ == '__main__':  
# Handle Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track= '#Bolivia')


# In[ ]:


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re

# Enter Twitter API Keys
access_token = "551693427-9YxBcOd49wE6nKhNCeVX0RKURlc0rSPEMov9FoPR"
access_token_secret = "UtKnwyytjObFs3RRXhVrIwruljYUB6xbCkzJf4nbzMVZf"
consumer_key = "7GKwhJwazdDrgaXSzZvMrFGtT"
consumer_secret = "ceLNls49QUtprrLCTDsjaXRLQJ4hGhKcIQKf4p7sfiXVcljZJM"

# Create tracklist with the words that will be searched for
tracklist = ['#ElMasNuncaMas', '#Bolivia']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 10

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):

    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=tracklist)


# In[ ]:




