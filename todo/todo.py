from . import data_access

class Todo:
    '''Todo is just this thing, you know?'''

    def __init__(self, description, id=None, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def save(self):
        '''Save this item and set the .id property.'''
        self.id = data_access.add_item(self.description)


def get_item(id):
    '''Get the Todo item that has the provided id. If no item
    exists with that id, return None.
    '''

    data = data_access.get_item(id)
    if data is not None:
        item = Todo(id=data[0],
                    description=data[1],
                    completed=data[2],
                    )
        return item
    else:
        return None
