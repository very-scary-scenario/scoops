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
                values = [f for f in [
                    l.decode('utf-8').strip() for l in fragfile.readlines()
                ] if f]

                for value in values:
                    count = len([v for v in values if v == value])
                    if count != 1:
                        raise ValueError(
                            '{value!r} appears {count} times in {name!r}'
                            .format(
                                value=value,
                                count=count,
                                name=name,
                            )
                        )

                setattr(self, name, values)


fragments = Fragments()
