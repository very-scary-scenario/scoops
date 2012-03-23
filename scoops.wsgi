#!/usr/bin/env python2

import os, sys

dir = os.path.dirname(__file__)

sys.path.append(dir)
os.chdir(dir)

import bottle
from random import choice
import re

import fragments

@bottle.route('/')

def index(name='Index'):
    franchise = '%s %s' % (choice(fragments.franchise_a), choice(fragments.franchise_b))
    company = choice(fragments.company)
       
    game_name = choice(fragments.name) % franchise
    story_raw = choice(fragments.story)
        
    order = re.findall('(?<=<).*?(?=>)', story_raw)
    first = order[0]

    # story = re.sub('<game>', game_name, re.sub('<company>', company, story_raw))
    story = re.split('<.*?>', story_raw)

    return bottle.template('gamename', story0=story[0], story1=story[1], story2=story[2], first=first, company=company, game=game_name)

application = bottle.default_app()
