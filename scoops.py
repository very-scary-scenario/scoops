#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from __future__ import unicode_literals

from random import choice, random
import re

from fragments import fragments


def get_fragment(name, html):
    if name == 'franchise':
        return u'%s %s' % (choice(fragments.franchise_a),
                           choice(fragments.franchise_b))

    if name == 'game':
        franchise = get_fragment('franchise', html)

        if random() < 0.4:
            game = choice(fragments.entry) % franchise
        else:
            game = franchise

        return u'<em>%s</em>' % game if html else u'‘%s’' % game

    else:
        return choice(getattr(fragments, name))


def make_story(html=True):
    story = choice(fragments.story)
    repl = {}
    for r in re.findall(r'<(.*?)>', story):
        if r not in repl:
            repl[r] = get_fragment(r.split('_')[0], html)

    for k, v in repl.iteritems():
        replacements = []
        if re.match(r'.*s\W*$', v):
            replacements.append(('<%s>’s' % k, '%s’' % v))

        replacements.append(('<%s>' % k, v,))

        for old, new in replacements:
            story = story.replace(old, new)

    return story

if __name__ == '__main__':
    from sys import argv
    tweet = 'tweet' in argv

    while True:
        story = make_story(html=False)
        if not tweet or len(story) <= 140:
            break

    if tweet:
        import tweepy

        from secrets import consumer_key, consumer_secret, key, secret

        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)

        api = tweepy.API(auth_handler=auth)
        api.update_status(story)

    else:
        print story
