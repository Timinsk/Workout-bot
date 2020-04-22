import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('workout.db')
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS loc_workout')

    c.execute('''
        CREATE TABLE IF NOT EXISTS loc_workout (
            id              INTEGER PRIMARY KEY,
            longitude       REAL,
            latitude        REAL,
            city            TEXT,
            score           INTEGER,
            count           INTEGER
        )''')

    conn.commit()


def add_message(user_id: int, text: str):
    conn = get_connection()
    c = get_connection()
    c.execute('INSERT INTO loc_workout (longitude, latitude, city) VALUES (?, ?)', (user_id, text))
    conn.commit()


if __name__ == '__main__':
    init_db()
