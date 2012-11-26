#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from random import choice
import re

import fragments
import tweepy

from sys import argv


def get_fragment(name, html):
    if name == 'franchise':
        return u'%s %s' % (choice(fragments.franchise_a), choice(fragments.franchise_b))

    if name == 'game':
        game = '%s' % choice(fragments.name) % get_fragment('franchise', html)
        if html: return u'<em>%s</em>' % game
        else: return u'‘%s’' % game

    else:
        return choice(getattr(fragments, name))

def make_story(html=True):
    story = choice(fragments.story)
    # print story
    repl = {}
    for r in re.findall(r'<(.*?)>', story):
        if r not in repl:
            repl[r] = get_fragment(r.split('_')[0], html)

    # print repl
    for r in repl:
        story = story.replace('<%s>' % r, repl[r])

    return story

if __name__ == '__main__':
    if 'tweet' in argv: tweet = True
    else: tweet = False

    while True:
        story = make_story(html=False)
        if not tweet or len(story) <= 140: break
    
    if tweet:
        from secrets import consumer_key, consumer_secret, key, secret
        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)

        api = tweepy.API(auth_handler=auth)
        api.update_status(story)

    else:
        print story
    
