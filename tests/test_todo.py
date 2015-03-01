import unittest
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
