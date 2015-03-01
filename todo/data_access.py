import sqlite3

CONNSTR = 'todo.db'


def init_db():
    '''Initialize the database by creating all necessary tables.'''
    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE
                        todo_item
                       (description text,
                        completed bool
                        )
                       ''')


def add_item(description):
    '''Add todo item and return the ID that is generated. The
    id may later be used to reference the item.
    '''

    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO
                        todo_item
                        (description,
                         completed)
                        VALUES
                         (?,
                          0)
                       ''', (description,))
        return cursor.lastrowid


def get_item(rowid):
    '''Return item that has the provided rowid. If no item is found
    with that id, return None.
    '''

    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT
                         description,
                         completed
                       FROM
                         todo_item
                       WHERE
                         rowid = ?
                       ''', (rowid,))
        row = cursor.fetchone()
        return row
