import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.node import nodeList

class participateTest(unittest.TestCase):
    
    def setUp(self):
        nodeList.NodeList.insertNode("localhost")
        pass

    def test_participate(self):
        test = {}
        operation.participate("localhost",test)
        #print(test)
        self.assertEqual(test["success"],1) 
if __name__ == '__main__':
    unittest.main()

