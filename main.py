import webapp2

class MainPage(webapp2.RequestHandler):
    def  get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.repsponse.out.write('Follow @polka__bot')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)