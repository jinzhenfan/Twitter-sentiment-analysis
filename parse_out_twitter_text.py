#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutTwitterText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read() #The read() method reads a string from an open file

    ### split off metadata
    content = all_text.split("X-FileName:") # split by string X-filename in the email code.
    words = ""
    if len(content) > 1: # X-filename exists, content[1] will be the email content
        ### remove punctuation
        translator = str.maketrans({key: None for key in string.punctuation}) 
        # for python 2.7, text_string = content[1].translate(string.maketrans("", ""), string.punctuation)
        text_string = content[1].translate(translator)
        print(text_string)
        ### project part 2: comment out the line below
        #words = text_string
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        word=text_string.split() # delete single space, save double space
        stemmer=SnowballStemmer("english")
        words=" ".join([stemmer.stem(ind_word) for ind_word in word])
        
    return words

    


