import unittest
import sys
sys.path.insert(0,'../../../')
from ds.db import data

class DataTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_getData(self):
        res=data.getData(1)
        print(res)
        self.assertIsNotNone(res)

    def test_insertData(self):
        res=data.insertData("hello")
        print(res)
        self.assertIsNotNone(res)

    def test_updateData(self):
        data.updateData(1,"halo")
        res = data.getData(1)
        print("test_updateDate : ",res)
        self.assertEqual(res["data"],"halo")

if __name__ == '__main__':
    unittest.main()

