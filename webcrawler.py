# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:16:41 2016

@author: 进击的樊
"""
###Using urllib
import urllib.request as ur
handle = ur.urlopen("http://www.usnews.com/")
html_gunk = handle.read()

###Using HTMLParser
from html.parser import HTMLParser

urlText = []
#Define HTML Parser
class parseText(HTMLParser):
        
    def handle_data(self, data):
        if data != '\n':
            urlText.append(data)
    

#Create instance of HTML parser
lParser = parseText()

#Feed HTML file into parser
lParser.feed(html_gunk.decode('utf-8'))
lParser.close()
for item in urlText:
    print (item)

#Simple scraping
###http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/web/simple_scraping.html