import unittest
import sys
sys.path.insert(0,'../../../')
from ds.node import data


class DataTest(unittest.TestCase):
    

    def test_setIdx(self):
        dataTest = data.Data()
        idx = 1
        dataTest.setIdx(idx)

        self.assertEqual(dataTest.getIdx(),idx)

    def test_setVersion(self):
        dataTest = data.Data()
        version = 1
        dataTest.setVersion(version)

        self.assertEqual(dataTest.getVersion(),version)

if __name__ == '__main__':
    unittest.main()
