import sqlite3

CONNSTR = 'todo.db'


def init_db():
    '''Initialize the database by creating all necessary tables.'''
    with sqlite3.connect(CONNSTR) as conn:
        pass
