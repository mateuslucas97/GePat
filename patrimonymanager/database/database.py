import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('credentials.db')
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS credentials (username TEXT, password TEXT)"""
        )
    except sqlite3.Error as e:
        print(e)


def insert_sample_credentials(conn):
    sample_credentials = [('admin', 'admin')]
    try:
        cursor = conn.cursor()
        cursor.executemany(
            'INSERT INTO credentials VALUES (?, ?)', sample_credentials
        )
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def get_valid_credentials(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM credentials')
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(e)
