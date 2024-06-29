#!/usr/bin/env python

""" Paul Graham's https://www.paulgraham.com/articles.html is like the gold-standard
    for article layouts so I shall follow suit.
"""
import datetime
import os
import re

REGEX = re.compile('\d{8}.md')
TAG = re.compile('<.*?>')


def strip_tags(line):
    """ Strip HTML tags.
    """
    return TAG.sub('', line)


def title(path):
    """ Extract first H1 line.
    """
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                return strip_tags(line[2:])
    return ''


if __name__ == '__main__':

    header = open('header.md', 'r').read()
    footer = open('footer.md', 'r').read()

    items = []

    for item in sorted(os.listdir('.'), reverse=True):
        match = REGEX.match(item)
        if match:
            blog = os.path.splitext(item)[0]
            date = datetime.datetime.strptime(blog, '%Y%m%d').strftime('%Y-%m-%d')
            desc = title(item)
            items.append(f'* [{date}](https://lcordier.github.io/blog/{blog}) {desc}')

    # Hehe, oldschool...
    open('README.md', 'w').write(header + '\n'.join(items) + footer)
