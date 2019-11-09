#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'c24b'
SITENAME = 'c24b'
SITEURL = 'c24b.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('InternetActu', 'http://internetactu.net'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/c4barbes'),
          ('Github', 'http://github.com/c24b'),)

DEFAULT_PAGINATION = 3
DEFAULT_DATE = (2019, 11, 9, 22, 22, 22)
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


STATIC_PATHS = [
    'static',
    'pdf',
    'extra/robots.txt',
]

THEME_STATIC_DIR = 'theme'
THEME = "attila"
PATH = 'content'
HEADER_COVER = '/themes/attila/static/cover.jpeg'
GITHUB_URL = "http://c24b.github.io"
# ARTICLE_PATHS = ['blog']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'

SOCIAL = (('twitter', 'https://twitter.com/c4barbes'),
          ('github', 'https://github.com/c24b'),
          ('gitlab', 'https://gitlab.com/c24b'),
          ('linkedin', 'https://linkedin.com/in/c4barbes'),
          ('envelope', 'mailto:4barbes@gmail.com'))

AUTHORS_BIO = {
    "c24b": {
        "name": "c24b",
        "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
        "website": "http://blog.arulraj.net",
        "location": "Paris",
        "bio": "Ingénieuse. Du code, des lettres et plus d'une corde à son sac"
    }
}
