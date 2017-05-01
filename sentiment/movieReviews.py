# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:16:20 2016

@author: 
""" 
###Save the data as csv file and import it to Tableau

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
#import word_feats.word_feats as WF
import sentiment.word_feats.word_feats as WF
def movie_pos_neg_classifier():
    
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
     
    negfeats = [(WF.word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
    posfeats = [(WF.word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
     
    negcutoff = int(len(negfeats)*3/4)
    poscutoff = int(len(posfeats)*3/4)
     
    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
    print ('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
     
    classifier = NaiveBayesClassifier.train(trainfeats)
    print ('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))    
    return classifier
movie_pos_neg_classifier().show_most_informative_features()