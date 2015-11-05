#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Rob Beagrie'
SITENAME = u"Rob Beagrie's Blog"
SITEURL = ''
DISQUS_SITENAME = 'robbeagriesblog'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom/all.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
SUMMARY_MAX_LENGTH = 50

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['theme/plugins']
PLUGINS = ['simple_footnotes', 'html_entity']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = "content"
STATIC_PATHS = ['images']

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
