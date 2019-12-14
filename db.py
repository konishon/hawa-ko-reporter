import sqlite3
from constants import DATABASE

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS subs (user_id TEXT, platform TEXT,is_subscribed bool,message_time TEXT default 8)')
    conn.close()

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


