# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 16:33:52 2016

@author: 进击的樊
"""
import sys
import pickle


FILE_NAME1 = "fetched_tweets_Turkish_60.txt"
FILE_NAME2="fetched_tweets_Pokemon_60.txt"
with open(FILE_NAME1, "r+") as data_file:
    content = data_file.read()