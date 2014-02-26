#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""models.py: Database tables and columns."""

import sqlite3

import config

connect = sqlite3.connect(config.DATABASE)
connect.row_factory = sqlite3.Row
cursor = connect.cursor()

# Companies:
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Companies(
        id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        description TEXT,
        uri TEXT,
        source TEXT
    );
    """
)

# Save to database:
connect.commit()
