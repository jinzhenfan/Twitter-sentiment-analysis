# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 23:49:20 2016

@author: Jinzhen
"""

import tweepy
import time
start_time = time.time()
time_limit=60

consumer_key="iup5Q41UMOW5VaF9vVb0Iw"
consumer_secret="Rj6oLpsMJICPk1wbEcPJwerstG4CH5xrIqnmZw0"
access_token="1962147962-cT85dOFlRa57RdElAox5Fn5sfgKt3NFVG7L2Lo1"
access_token_secret=	"nKGWdb3czLqYmWlR9CJVHnU6NkIv0QufzHbBOnBcrs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
###https://github.com/tweepy/tweepy/blob/78d2883a922fa5232e8cdfab0c272c24b8ce37c4/tweepy/streaming.py
    def on_status(self, status):
        ###if status.filter(locations=[-121.791399,38.533554,-121.670890,38.593157], async=True)
        ###status.geo!=None        
        ###if (status.geo!=None and 'pokemon' in status.text.lower()):
        if (status.geo!=None and 'pokemon' in status.text.lower()):
            print(status.geo['coordinates'], status.text)  ###return latitude and longitude coordinates
        #print(status.text) stackoverflow.com/questions/7714282/return-actual-tweets-in-tweepy
        if ((time.time() - start_time) < time_limit):  
            with open('tweets_pokemon_catch4.txt','a') as tf:
                tf.write(status.text)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print("error")
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#location_stream= myStream.filter(locations=[-122.75,36.8,-121.75,37.8], async=True)
#location_stream= myStream.filter(locations=[-122.75,36.8,-121.75,37.8])
#[-121.79,38.53,-121.67,38.59]
key_filtered_stream=myStream.filter(track=['Pokemon catch', 'Pokemon caught'])
#myStream.disconnect()
#key_filtered_stream=myStream.filter(track=['injury Pokemon','kill Pokemon','safety Pokemon'])
#myStream.filter(locations=[-180,-90,180,90], async=True)
