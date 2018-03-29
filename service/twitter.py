from google.appengine import api

import base
import json
import re
import urllib
import urllib2
import oauth2 as oauth

consumer_key = 'fG0hDKhIDmOIYlmL5trQ'
consumer_secret = 'vVzzrl8pqeizu8X0ANyTJrxAhv73PDoTLktk0OW7g'

request_token_url = 'https://twitter.com/oauth/request_token'
access_token_url = 'https://twitter.com/oauth/access_token'
authorize_url = 'https://twitter.com/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

def fetchbyID(term):
    resp, content = client.request('https://api.twitter.com/1.1/statuses/show.json?id=' + urllib2.quote(term), 'GET')
    if resp['status'] != '200':
        return 'Could not reach Twitter API.'

    return content


def fetchbyUserName(term):
    resp, content = client.request("https://api.twitter.com/1.1/statuses/user_timeline.json?count=1&screen_name=" + term, "GET")
    if resp['status'] != '200':
        return 'Could not reach Twitter API.'
    try:
        json_content = json.loads(content)
    except:
        return 'Could not make sense of data from Twitter API.'

    #return format_tweet(json_content[0])
    return json.dumps(json_content[0])


def fixURLs(jcont, text):
    out_text = text
    list_of_urls = jcont['entities']['urls']
    for url in list_of_urls:
        if url['url'] in out_text:
            out_text = out_text.replace(url['url'], url['expanded_url'])
    return out_text


def format_tweet(content):
    txt = fixURLs(content, content['text'])
    posted = content['created_at']
    fav_count = content['favorite_count']
    rt_count = content['retweet_count']
    name = content['user']['screen_name']

    return '{1} | By: @{0}, Date: {2}, RT#: {3}, Favs: {4}'.format(name, txt, posted, rt_count, fav_count)


class Main(base.RequestHandler):

    def get(self,*args):
        # Args is just a string...
        # well, args[1] anyway
        arg = None
        try:
            arg = args[1]
        except IndexError:
            pass
        if not arg:
            return self.ok("You must supply a username or something.")

        params = urllib.unquote(arg).strip().split()      # split on whitespace.

        if len(params) == 1:
            # Only one parameter.  By default a username.  Also allow
            # a twitter URL (distinguished by http:// of course) or an id
            # number
            term = params[0]
            ans = None
            if term.startswith('http'):
                # http://twitter.com/username/status/46611258765606912
                m = re.match(r'https?://(?:www\.)?twitter\.com/\w*/status/(\d+)',
                           term)
                if not m:
                    return self.ok("Could not parse twitter url.")

                return self.ok(fetchbyID(m.group(1)))

            if term.isdigit():
                # This enough to tell if it's a status id#?  Is it possible
                # to have a username that's all numbers?
                ## stays the same
                return self.ok(fetchbyID(term))
            else:
                # Otherwise, a user.
                # Should I check if its all alnum or something?  Probably.
                #if not term.isalnum():
                #    return self.ok("%s did not look like a username." % term)
                return self.ok(fetchbyUserName(term))
        elif len(params)==2:
            # two params means user and status id, which is the same as
            # just status id.
            return self.ok(fetchbyID(params[1]))
        else:
            return self.ok("??")
