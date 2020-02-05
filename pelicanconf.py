#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Giacomo Caironi"
SITENAME = "Giacomo Caironi"
SITEURL = ""

THEME = "./Bootstrap-dark"

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

PAGE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}.html"
CATEGORY_URL = "{slug}.html"
CATEGORY_SAVE_AS = "{slug}.html"
ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"
TAG_URL = "tag/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"

# DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
DIRECT_TEMPLATES = ["index", "categories", "tags"]

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/giacomocaironi"),
    (
        "Coding game",
        "https://www.codingame.com/profile/47ba85ec52c5209c85ee6dea92e4a5a53356353",
    ),
    ("Project Euler", "https://projecteuler.net/profile/CairoJack.png"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
