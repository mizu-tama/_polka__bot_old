# -*- coding: utf-8 -*-
import webapp2
from twitter import TwitterAuth

class PolkaBot(webapp2.RequestHandler):
    def get(self):
        self.post("だれかきたよ！")
        
    def post(self, tweet):
        twitter = TwitterAuth()
        twitter.post(tweet)