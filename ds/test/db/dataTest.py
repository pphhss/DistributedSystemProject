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

    def test_getDataFromKey(self):
        data.insertData('p1','hs')
        res = data.getDataFromKey('p')
        self.assertEqual(res['v'],'hs')

    def test_insertData(self):
        res=data.insertData("q1",'hs')
        print(res)
        self.assertIsNotNone(res)

    def test_updateValue(self):
        data.insertData('g1','hss')
        data.updateValue('g',"halo")
        res = data.getDataFromKey('g')
        print("test_updateDate : ",res)
        self.assertEqual(res["v"],"halo")

if __name__ == '__main__':
    unittest.main()

