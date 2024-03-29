# -*- coding: utf-8 -*-
import webapp2
import jinja2
import os
from bot.polkabot import PolkaBot

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def  get(self):
        template = jinja_env.get_template('/templates/index.html')
        self.response.out.write(template.render())
        
class InTheRoom(webapp2.RequestHandler):
    def  get(self):
        template = jinja_env.get_template('/templates/room.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication(
                [('/', MainPage),
                ('/post', PolkaBot),
                ('/room', InTheRoom)],                            
                debug=True)