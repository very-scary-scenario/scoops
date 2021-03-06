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
                    line.strip() for line in fragfile.readlines()
                ] if f]

                for value in values:
                    count = len([v for v in values if v == value])

                    for banned_character in ["'", '"']:
                        if banned_character in value:
                            raise ValueError(
                                "You should be using ’ rather than ' in {0!r}"
                                .format(value)
                            )

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
