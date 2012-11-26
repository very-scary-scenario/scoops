#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os, sys

dir = os.path.dirname(__file__)

sys.path.append(dir)
os.chdir(dir)

import bottle

from scoops import make_story

@bottle.route('/')
def index(name='Index'):
    story = make_story().replace('&', '&amp;')

    return bottle.template('gamename', story=story)

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)
    #from flup.server.fcgi import WSGIServer
    #WSGIServer(application).run()
