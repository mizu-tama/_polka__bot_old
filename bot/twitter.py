# -*- coding: utf-8 -*-
import tweepy
import config as cnf

class TwitterAuth(object):
    def getApi(self):
        auth = tweepy.OAuthHandler(cnf.consumer_key, cnf.consumer_secret)
        auth.set_access_token(cnf.access_key, cnf.access_secret)
        api =  tweepy.API(auth_handler=auth)
        return api

    def post(self, tweet):
        api = self.getApi()
        api.update_status(tweet)