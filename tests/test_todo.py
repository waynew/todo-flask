import unittest
import unittest.mock as mock
import todo.todo as todo


class TestTodo(unittest.TestCase):
    def test_when_todo_is_created_the_id_should_be_None(self):
        item = todo.Todo('ignore this description')

        self.assertIsNone(item.id, "New item should have id of None")

    def test_when_todo_is_created_description_should_be_set(self):
        expected_desc = 'This is the most todo-y todo ever'
        item = todo.Todo(description=expected_desc)

        self.assertEqual(expected_desc, item.description)

    def test_when_todo_is_created_completed_should_be_False(self):
        item = todo.Todo(description='fnord')

        self.assertFalse(item.completed, "Completed should be False")

    @mock.patch('todo.data_access.add_item')
    def test_when_todo_save_is_called_id_should_be_set(self, mock_add_item):
        item = todo.Todo(description='whatever')

        item.save()

        self.assertIsNotNone(item.id, "Item id should be set")

    @mock.patch('todo.data_access.add_item')
    def test_when_todo_save_is_called_id_should_be_set_to_result_of_data_access_call(self, mock_add_item):
        expected_id = 42

        mock_add_item.return_value = expected_id
        item = todo.Todo(description='your father smelled of elderberry')

        item.save()

        self.assertEqual(expected_id, item.id,
                         'Item id should have been set to result of call')

    @mock.patch('todo.data_access.get_item')
    def test_when_todo_get_item_is_called_and_data_access_returns_None_it_should_return_None_too(self, mock_get_item):
        mock_get_item.return_value = None

        self.assertIsNone(todo.get_item(42),
                          'get_item should have returned None')

    @mock.patch('todo.data_access.get_item')
    def test_when_todo_get_item_is_called_and_data_access_returns_data_Todo_should_have_same_values(self, mock_get_item):
        expected_id = 1337
        expected_desc = "h4><0r"
        expected_completed = False
        mock_get_item.return_value = (expected_id,
                                      expected_desc,
                                      expected_completed)

        item = todo.get_item(expected_id)

        self.assertEqual(expected_id, item.id)
        self.assertEqual(expected_desc, item.description)
        self.assertEqual(expected_completed, item.completed)
