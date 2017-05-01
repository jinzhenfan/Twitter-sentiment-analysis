# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:23:02 2016

@author: 
"""
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
#import word_feats.word_feats as WF
import sentiment.word_feats.word_feats as WF
twitter_samples.fileids()
"""

word=twitter_samples.tokenized('positive_tweets.json')
stemmer=SnowballStemmer("english")
words=list([stemmer.stem(ind_word) for ind_word in word])

strings = twitter_samples.strings('tweets.20150430-223406.json')
for string in strings[:15]:
    print(string)
    """
def twitter_pos_neg_classifier():
    
    pos_tweets=twitter_samples.strings('positive_tweets.json')
    neg_tweets=twitter_samples.strings('negative_tweets.json') 
    ##stemming, filtering, removing stopwords and numbers
    negfeats = [(WF.word_feats(f.split()), 'neg') for f in neg_tweets][:1000]
    posfeats = [(WF.word_feats(f.split()), 'pos') for f in pos_tweets][:1000]
    #split features
    negcutoff = int(len(negfeats)*3/4)
    poscutoff = int(len(posfeats)*3/4)
     
    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    print ('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
     
    classifier = NaiveBayesClassifier.train(trainfeats)
    print ('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
    return classifier

twitter_pos_neg_classifier().show_most_informative_features()