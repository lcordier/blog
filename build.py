#!/usr/bin/env python

""" Paul Graham's https://www.paulgraham.com/articles.html is like the gold-standard
    for article layouts so I shall follow suit.
"""
import os
import re

REGEX = re.compile('\d{8}.md')

if __name__ == '__main__':

    header = open('header.md', 'r').read()
    footer = open('footer.md', 'r').read()

    items = []

    for item in sorted(os.listdir('.')):
        match = REGEX.match(item)
        if match:
            blog = os.path.splitext(item)[0]
            items.append(f'* [{blog}](https://lcordier.github.io/blog/{blog})')

    # Hehe, oldschool...
    open('README.md', 'w').write(header + '\n'.join(items) + footer)
