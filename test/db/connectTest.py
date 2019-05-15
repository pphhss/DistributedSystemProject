import unittest
import sys
sys.path.insert(0,'../../db')
import connect

class ConnectDBTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_getCursor(self):
        cursor = connect.Connection.getCursor()
        self.assertIsNotNone(cursor)

if __name__ == '__main__':
    unittest.main()


