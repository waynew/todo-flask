import unittest
import unittest.mock
import todo.data_access as data_access


class TestDataAccess(unittest.TestCase):
    def test_when_CONNSTR_is_changed_it_should_be_used_to_init_db(self):
        expected_CONNSTR = 'all-your-base'
        with unittest.mock.patch('todo.data_access.sqlite3') as fake_sqlite:
            data_access.CONNSTR = expected_CONNSTR
            data_access.init_db()

        fake_sqlite.connect.assert_called_once_with(expected_CONNSTR)
