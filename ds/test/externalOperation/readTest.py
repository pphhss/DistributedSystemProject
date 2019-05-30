import unittest
import sys
sys.path.insert(0, '../../../')
from ds.node import nodeList
from ds.externalOperation import externalOperation as exop
from ds import config

class ExternalReadTest(unittest.TestCase):

    def setUp(self):
        self.key = "exopInsertTest5"
        pass

    def test_isWorkInNodeList(self):
        res = exop.read(self.key)
        print(res)
        self.assertEqual(res,"hi")


if __name__ == '__main__':
    unittest.main()
