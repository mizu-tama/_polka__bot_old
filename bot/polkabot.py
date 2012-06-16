# -*- coding: utf-8 -*-
import webapp2
from twitter import TwitterAuth

class PolkaBot(webapp2.RequestHandler):
    def get(self):
        self.post("GAEでつぶやくてすと")
        
    def post(self, tweet):
        twitter = TwitterAuth()
        twitter.post(tweet)