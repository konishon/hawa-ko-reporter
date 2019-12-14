import sqlite3
from constants import DATABASE


def init_db():
    """
    create a db if it does not exist
    """
    conn = sqlite3.connect(DATABASE)
    conn.execute(
        'CREATE TABLE IF NOT EXISTS subs (user_id TEXT, platform TEXT,is_subscribed bool,message_time TEXT default 8)')
    conn.close()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except error as e:
        print(e)

    return conn


def select_subs_by_platform(platform):
    '''
    fetches all active subscribers with using viber
    returns ('ASAu+ASAkkqIdJASAvzX==', 'viber', 1, '8')
    '''
    conn = create_connection(DATABASE)
    raw_query = '''SELECT * FROM subs WHERE platform='{0}' AND is_subscribed={1}
    '''.format(
        "viber",
        1)
    print("[INFO] {}".format(raw_query))
    rows = query(conn, raw_query=raw_query)
    
    return rows


def query(conn, raw_query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(raw_query)

    rows = cur.fetchall()
    x = len(rows)
    print(x)
    for row in rows:
        print(row)
    return rows
