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


def add_item(decription):
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
                          false)
                       ''')
        return cursor.lastrowid
