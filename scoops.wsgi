#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os, sys

dir = os.path.dirname(__file__)

sys.path.append(dir)
os.chdir(dir)

import bottle
from random import choice
import re

import fragments


def get_fragment(name):
    if name == 'franchise':
        return '%s %s' % (choice(fragments.franchise_a), choice(fragments.franchise_b))

    if name == 'game':
        return u"“%s”" % choice(fragments.name) % get_fragment('franchise')

    else:
        return choice(getattr(fragments, name))

def make_story():
    story= choice(fragments.story)
    repl = {}
    for r in re.findall(r'<(.*?)>', story):
        if r not in repl:
            repl[r] = get_fragment(r.split('_')[0])

    for r in repl:
        story = story.replace('<%s>' % r, repl[r])

    return story

@bottle.route('/')
def index(name='Index'):
    story = make_story()

    return bottle.template('gamename', story=story)

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
    #from flup.server.fcgi import WSGIServer
    #WSGIServer(application).run()
