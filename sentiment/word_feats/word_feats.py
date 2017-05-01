# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:08:37 2016

@author: Jinzhen
"""
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
###clean up punctuation, stopwords, numbers

def word_feats(words):
    stemmer=SnowballStemmer("english")
    stop = stopwords.words('english')
    return dict([(stemmer.stem(word), True) for word in words if (word not in string.punctuation) and (word not in stop) and word.isdigit()==False])
    #return dict([(word, True) for word in words if (word not in string.punctuation) 
