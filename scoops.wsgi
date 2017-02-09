#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import os

d = os.path.realpath(os.path.dirname(__file__))

sys.path.append(d)
os.chdir(d)

import bottle

from scoops import make_story


@bottle.route('/')
def index(name='Index'):
    story = make_story().replace('&', '&amp;')

    return bottle.template('gamename', story=story)


@bottle.route('/ticker')
def ticker(name='Ticker'):
    return bottle.template('ticker')


@bottle.route('/raw')
def raw(name='Raw'):
    try:
        count = int(bottle.request.query.count)
    except ValueError:
        count = 1

    html = bool(bottle.request.query.html)

    bottle.response.content_type = 'text/plain; charset=utf-8'

    return '\n'.join([
        make_story(html=html) for x in xrange(min(500, count))
    ])

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='localhost', port=8081)
    # from flup.server.fcgi import WSGIServer
    # WSGIServer(application).run()
