import sqlite3
from constants import DATABASE


def get_db(g):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(g,query, args=(), one=False):
    cur = get_db(g).execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


