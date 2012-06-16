# -*- coding: utf-8 -*-
import tweepy
import config as cnf

oauth = tweepy.OAuthHandler(cnf.consumer_key, cnf.consumer_secret)
oauth.set_access_token(cnf.access_key, cnf.access_secret)

api =  tweepy.API(auth_handler=oauth)

api.update_status("はじめてのつぶやき")