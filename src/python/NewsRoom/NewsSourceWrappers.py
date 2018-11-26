#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from newsapi import NewsApiClient
import requests


class AbstractNewsWrapper(object):
    '''This is where all of the code
    for things related to all news wrappers
    will go. Will include:
    - Mapping articles to places
    - Relating articles between sites
    - Mining an article for keywords'''

    def __init__(self, key):
        self.__key = key
        self.newsapi = NewsApiClient(api_key=key)

    def __handle_text_encodings__(self, text):
        """This is a helper function as I work on getting the encodings down.
        It will handle things like utf-8 to ascii"""
        return text.decode('utf-8', 'ignore')


    def get_top_stories(self):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + self.id + '&'
                                      'language=en&'
                                      'apiKey=' + self.__key)
        response = requests.get(url)
        return response.json()

    def get_everything(self):
        url = ('https://newsapi.org/v2/everything?'
               'sources=' + self.id + '&'
                                      'language=en&'
                                      'apiKey=' + self.__key)
        response = requests.get(url)
        return response.json()

    def get_all_article_titles(self):
        top = [self.__handle_text_encodings__(json.dumps(top_story["title"]))
               for top_story in self.get_top_stories()["articles"]]
        everything = [self.__handle_text_encodings__(json.dumps(top_story["title"]))
                      for top_story in self.get_everything()["articles"]]
        return top + everything



class NewYorkTimesWrapper(AbstractNewsWrapper):
    """A specific wrapper on the NYTimes"""
    id = "the-new-york-times"


class FoxNewsWrapper(AbstractNewsWrapper):
    """A specific wrapper on Fox News"""
    id = "fox-news"


# key = 'dfb01964eddf453eaec25e3ee977395b'
#
# nyt = NewYorkTimesWrapper(key)
# fox = FoxNewsWrapper(key)
#
# for nyt_story in nyt.get_all_article_titles():
#     print nyt_story
#
# for fox_story in fox.get_all_article_titles():
#     print fox_story

print '\u2019'.encode('ascii')
print '\u2019'.encode('utf-8')
print '\u2019'.decode('utf-8')
print '\u2019'.decode('ascii')
