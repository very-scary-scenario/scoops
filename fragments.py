# -*- coding=utf-8 -*-

import os


DIR = os.path.join(
    os.path.dirname(__file__),
    'fragments',
)


class Fragments(object):
    def __init__(self):
        for filename in os.listdir(DIR):
            name, ext = os.path.splitext(filename)
            if ext != '.txt':
                continue

            with open(os.path.join(DIR, filename)) as fragfile:
                setattr(self, name, [
                    f for f in [
                        l.strip() for l in fragfile.readlines()
                    ] if f
                ])


fragments = Fragments()
