#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""config.py: Default configuration."""

import os

# Paths:
ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATES = '{base}/templates'.format(base=ROOT)
DATABASE = '{base}/db.sqlite3'.format(base=ROOT)
SESSION = '{base}/session'.format(base=ROOT)

# Server:
BASE_URI = 'http://mydomain.tld'
SERVER = 'wsgiref'
HOST = 'localhost'
PORT = 8000
RELOADER = True

# Session:
SESSION_TYPE = 'file'
SESSION_AUTO = True

# Facebook:
FACEBOOK_CLIENT_ID = '545723862164937'
FACEBOOK_CLIENT_SECRET = '5407608c6e9d10b297ba77a4de18f75f'
