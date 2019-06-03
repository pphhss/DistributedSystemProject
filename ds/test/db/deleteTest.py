import unittest
import sys
sys.path.insert(0,'../../../')
from ds.db import data

class DataTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_getData(self):
        data.deleteAllData()
        

if __name__ == '__main__':
    unittest.main()

