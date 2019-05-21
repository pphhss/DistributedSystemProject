import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation

class InsertTest(unittest.TestCase):

    def setUp(self):
        pass
    def test_insert(self):
        res = operation.insert("this is fucking day!")
        print("response result : ",res)
        self.assertIsNotNone(res)
if __name__ == '__main__':
    unittest.main()

