#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'brett rudder'
SITENAME = 'brudder-site'
SITEURL = ''
SITETITLE = "I'm interested in Machine Learning and AI"

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'General'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Paths
STATIC_PATHS = ['images', 'authors']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/yourprofile'),
         ('instagram', 'https://instagram.com/yourprofile'),
         ('github', 'https://github.com/yourprofile'))

SHARE_BUTTONS = ('twitter', 'facebook', 'whatsapp', 'mail')

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 70

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './themes/minimalX'

TAG_CLOUD = True
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
TAG_CLOUD_BADGE = True
TAG_CLOUD_SORTING = 'size'

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "autopages"]
