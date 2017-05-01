import tweepy
import datetime
from PyQt4.QtCore import QVariant

consumer_key="iup5Q41UMOW5VaF9vVb0Iw"
consumer_secret="Rj6oLpsMJICPk1wbEcPJwerstG4CH5xrIqnmZw0"
access_token="1962147962-cT85dOFlRa57RdElAox5Fn5sfgKt3NFVG7L2Lo1"
access_token_secret=	"nKGWdb3czLqYmWlR9CJVHnU6NkIv0QufzHbBOnBcrs"
key = tweepy.OAuthHandler(consumer_key, consumer_secret)
key.set_access_token(access_token, access_token_secret)

# here come the tweepy part:

class stream2lib(tweepy.StreamListener):
    output = {}
    def __init__(self, api=None):
        api = tweepy.API(key)
        self.api = api or API()
        self.n = 0
        self.m = 10
    def on_status(self, status):
        self.output[status.id] = {
            'tweet':status.text.encode('utf8'),
            'user':status.user.screen_name.encode('utf8'),
            'geo':status.geo,
            'localization':status.user.location,
            'time_zone':status.user.time_zone,
            'time':status.timestamp_ms}
        if self.output[status.id]['geo']!=None:
            self.n = self.n+1
            print ("Tweet found")
        if self.n < self.m: 
            return True
        else:
            return False
stream = tweepy.streaming.Stream(key, stream2lib()) #initiate the stream
stream.filter(locations=[5.0770, 47.2982, 15.0403, 54.9039]) #filter the stream for tweets in this "box"
tweetdic = stream2lib().output #copy it in a variable
print (tweetdic)
vl = QgsVectorLayer("Point", "temporary_twitter_results", "memory")
pr = vl.dataProvider()
# changes are only possible when editing the layer
vl.startEditing()
# add fields
pr.addAttributes([QgsField("user_name", QVariant.String),QgsField("localization", QVariant.String),QgsField("tweet", QVariant.String), QgsField("time", QVariant.String)])
# add a feature


for tweet in tweetdic:
    if tweetdic[tweet]['geo'] != None:
        fet = QgsFeature() #it's a new feature
        fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(tweetdic[tweet]['geo']['coordinates'][1],tweetdic[tweet]['geo']['coordinates'][0] ))) #use the coordinates for point location
        tweettime = datetime.datetime.utcfromtimestamp(float(tweetdic[tweet]['time'][:-3] + "." + tweetdic[tweet]['time'][11:13])).strftime('%Y-%m-%d %H:%M:%S:%f') #parse the time to fit YYYY-MM-DD HH:MM:SS:MS
        fet.setAttributes([tweetdic[tweet]['user'],tweetdic[tweet]['localization'],tweetdic[tweet]['tweet'],tweettime]) #set attributes of current tweet at current location
        pr.addFeatures([fet]) #and add the feature to the layer.
# commit to stop editing the layer
vl.commitChanges()
# update layer's extent when new features have been added
# because change of extent in provider is not propagated to the layer
vl.updateExtents()
QgsMapLayerRegistry.instance().addMapLayer(vl)
