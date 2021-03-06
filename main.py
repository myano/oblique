import webapp2

import wsgiref.handlers

from google.appengine.ext import webapp

import django

from service import base
from service import mirror
from service import identica
from service import lastfm
from service import fact
from service import steps
from service import soccer
from service import stupid
from service import ticket
from service import unicode
from service import entity
from service import internet
from service import vary
from service import googlesets
from service import search
from service import connect
from service import isbn
from service import dwim
from service import whois
from service import speak
from service import py
from service import wolframalpha
from service import fourchan
from service import wow
from service import map
from service import general
from service import jargon

uris = [
  ("^/$", base.Index),
  ("^/mirror(/.*?)?", mirror.Main),
  ("^/identica(/(.*?))?(/(.*?))?/?", identica.Main),
  ("^/lastfm(/(.*?))?(/(.*?))?/?", lastfm.Main),
  ("^/fact(/(.*?))?/?", fact.Main),
  ("^/soccer(/(.*?))?/?", soccer.Main),
  ("^/steps(/(.*?))?/?", steps.Main),
  ("^/stupid(/(.*?))?/?", stupid.Main),
  ("^/ticket(/(.*?))?(/(.*?))?/?", ticket.Main),
  ("^/internet(/(.*?))?/?", internet.Main),
  ("^/unicode(/(.*?))?/?", unicode.Main),
  ("^/entity(/(.*?))?/?", entity.Main),
  ("^/vary(/(.*?))?/?", vary.Main),
  ("^/sets(/(.*?))?/?", googlesets.Main),
  ("^/search(/(.*?))?/?", search.Main),
  ("^/connect(/(.*?))?/?", connect.Main),
  ("^/isbn(/(.*))?/?", isbn.Main),
  ("^/dwim(/(.*))?/?", dwim.Main),
  ("^/whois(/(.*))?/?", whois.Main),
  ("^/speak(/(.*))?/?", speak.Main),
  ("^/py(/(.*))?/?", py.Main),
  ("^/wa(/(.*))?/?", wolframalpha.Main),
  ("^/4chan/?", fourchan.Main),
  ("^/wow(/(.*?))?/?", wow.Main),
  ("^/map(/(.*?))?/?", map.Main),
  ("^/general(/(.*?))?/?", general.Main),
  ("^/jargon(/(.*?))?/?", jargon.Main),
  ("^/.*$", base.NotFound),
]

def main():
  wsgiref.handlers.CGIHandler().run(webapp.WSGIApplication(uris, debug=True))

'''class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, WebApp World!')
'''

#app = webapp2.WSGIApplication([('/', MainPage)])

if __name__ == "__main__":
    main()
