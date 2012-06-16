# -*- coding: utf-8 -*-
import webapp2
from bot.polkabot import PolkaBot

class MainPage(webapp2.RequestHandler):
    def  get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Follow @polka__bot')

app = webapp2.WSGIApplication(
                [('/', MainPage),
                ('/post', PolkaBot)],                                
                debug=True)