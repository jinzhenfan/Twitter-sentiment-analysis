# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 23:49:20 2016

@author: Trained by movie reviews
"""

import tweepy
import time
import os
import sys
import sentiment.movieReviews as Movie
import sentiment.twitter_samples as Twitt
import sentiment.word_feats.word_feats as WF
#import json
start_time = time.time()
time_limit=60

consumer_key="iup5Q41UMOW5VaF9vVb0Iw"
consumer_secret="Rj6oLpsMJICPk1wbEcPJwerstG4CH5xrIqnmZw0"
access_token="1962147962-cT85dOFlRa57RdElAox5Fn5sfgKt3NFVG7L2Lo1"
access_token_secret=	"nKGWdb3czLqYmWlR9CJVHnU6NkIv0QufzHbBOnBcrs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
    """
tweets = []
save_file = open('13may.json', 'a')
clf0=Movie.movie_pos_neg_classifier()
clf1=Twitt.twitter_pos_neg_classifier()

class MyStreamListener(tweepy.StreamListener):
###https://github.com/tweepy/tweepy/blob/78d2883a922fa5232e8cdfab0c272c24b8ce37c4/tweepy/streaming.py
    def __init__(self, api):
        self.api = api or API()
        super(tweepy.StreamListener, self).__init__()
        self.save_file = tweets
        self.n = 0
        self.m = 200 
        self.MoviePos=0
        self.MovieNeg=0
        self.TwittPos=0
        self.TwittNeg=0

    """
    def on_data(self, tweet):

        self.save_file.append(json.loads(tweet))
        #print (tweet)
        save_file.write(str(tweet))
        """

    def on_status(self, status):
        if ('pokemon' in status.text.lower()):
            #print (status.text[1:].encode('utf8'))
            print (status.text)
            sentiment_result_0=clf0.classify(WF.word_feats(status.text.split()))
            sentiment_result_1=clf1.classify(WF.word_feats(status.text.split()))
            if (sentiment_result_0=='neg'):
                self.MovieNeg=self.MovieNeg+1
            if (sentiment_result_0=='pos'):
                self.MoviePos=self.MoviePos+1  
            if (sentiment_result_1=='neg'):
                self.TwittNeg=self.TwittNeg+1
            if (sentiment_result_1=='pos'):
                self.TwittPos=self.TwittPos+1
            if (sentiment_result_0=='neg' and sentiment_result_1=='pos'):
                print(sentiment_result_0,sentiment_result_1)
            #print("Movie_Reviews trained pos:neg ", self.MoviePos, ":", self.MovieNeg)
            #print("Twitter_Samples trained pos:neg ", self.TwittPos, ":", self.TwittNeg)            
            self.n = self.n+1
        if self.n < self.m: return True
        else:
            print ('tweets = '+str(self.n))
            return False
        
    """ 
        #if ((time.time() - start_time) < time_limit ):  
            #with open('tweets_pokemon_catch5.txt','a') as tf:
             #   tf.write(status.text)
        if ((time.time() - start_time) < time_limit):  
        """
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print("error")
            return False
        
myStreamListener = MyStreamListener(api)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#location_stream= myStream.filter(locations=[-122.75,36.8,-121.75,37.8], async=True)
#location_stream= myStream.filter(locations=[-122.75,36.8,-121.75,37.8])
#[-121.79,38.53,-121.67,38.59]
key_filtered_stream=myStream.filter(locations=[-127.597019, 32.375215, -60.953617,48.152158])
#myStream.disconnect()
#key_filtered_stream=myStream.filter(track=['injury Pokemon','kill Pokemon','safety Pokemon'])
#myStream.filter(locations=[-180,-90,180,90], async=True)