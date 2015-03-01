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


def get_item(id):
    '''Return item that has the provided id. If no item is found
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
                       ''', (id,))
        row = cursor.fetchone()
        return row


def complete_item(id):
    '''Mark item completed that matches the provided id. If no item
    matches that ID, raise KeyError.
    '''

    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       UPDATE
                         todo_item
                       SET
                         completed
                       =
                         1
                       WHERE
                         rowid = ?
                       ''', (id,))

        if cursor.rowcount == 0:
            raise ValueError("No todo_item with id <{}>".format(id))


def delete_item(id):
    '''Delete an item with the provided id. If no item is found with that
    id, raise ValueError.'''

    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       DELETE FROM
                         todo_item
                       WHERE
                         rowid = ?
                       ''', (id,))

        if cursor.rowcount == 0:
            raise ValueError("No todo_item with id <{}>".format(id))


def list_items(completed=None):
    '''List todo items. If completed is None, return all items. If completed
    is True, return completed items. If completed is False, return only
    uncompleted items.
    '''

    with sqlite3.connect(CONNSTR) as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT
                         rowid,
                         description,
                         completed
                       FROM
                         todo_item
                       ''')
        items = []
        for row in cursor.fetchall():
            items.append((row[0],
                          row[1],
                          bool(row[2]),
                          ))
        return items
