import sqlite3
import unittest
import tempfile
import unittest.mock
import todo.data_access as data_access


class TestDataAccess(unittest.TestCase):
    def test_when_CONNSTR_is_changed_it_should_be_used_to_init_db(self):
        expected_CONNSTR = 'all-your-base'
        with unittest.mock.patch('todo.data_access.sqlite3') as fake_sqlite:
            data_access.CONNSTR = expected_CONNSTR
            data_access.init_db()

        fake_sqlite.connect.assert_called_once_with(expected_CONNSTR)

    def test_when_init_db_is_called_it_should_create_table(self):
        try:
            with tempfile.NamedTemporaryFile() as f:
                data_access.CONNSTR = f.name
                data_access.init_db()

                with sqlite3.connect(f.name) as conn:
                    cursor = conn.cursor()
                    cursor.execute('SELECT * FROM todo_item')
        except sqlite3.OperationalError:
            self.fail("Should not have raised sqlite3.OperationalError")

    def test_when_add_item_is_called_it_should_return_an_id(self):
        expected_rowid = 42
        with unittest.mock.patch('todo.data_access.sqlite3') as fake_sqlite:
            fake_conn = unittest.mock.MagicMock()
            fake_cursor = unittest.mock.MagicMock()
            fake_sqlite.connect.return_value = fake_conn
            fake_conn.cursor.return_value = fake_cursor

            self.assertIsNotNone(data_access.add_item("Make this test work"))

    def test_get_item_after_add_item_should_return_inserted_value(self):
        expected_desc = 'This test is awesome'
        with tempfile.NamedTemporaryFile() as f:
            data_access.CONNSTR = f.name
            data_access.init_db()
            row_id = data_access.add_item(expected_desc)

            desc, completed = data_access.get_item(row_id)

            self.assertEqual(desc, expected_desc,
                             "Description should be the one provided")
            self.assertFalse(completed, 'Completed should be false on new item')

    def test_get_item_with_bogus_rowid_should_return_None(self):
        expected_desc = 'This test is awesome'
        with tempfile.NamedTemporaryFile() as f:
            data_access.CONNSTR = f.name
            data_access.init_db()

            self.assertIsNone(data_access.get_item('whatever'),
                             "Item should be None if not found")


    def test_complete_item_then_get_item_should_be_completed(self):
        with tempfile.NamedTemporaryFile() as f:
            data_access.CONNSTR = f.name
            data_access.init_db()
            id = data_access.add_item('Not important')

            data_access.complete_item(id)

            _, completed = data_access.get_item(id)

            self.assertTrue(completed, "Item should've been marked complete")

    def test_complete_item_on_bad_id_should_ValueError(self):
        with tempfile.NamedTemporaryFile() as f:
            data_access.CONNSTR = f.name
            data_access.init_db()

            with self.assertRaises(ValueError):
                data_access.complete_item(42)
