import unittest
import sys
sys.path.insert(0,'../../../')
from ds.node import node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = node.Node(1,"192.168.133.33")

    def test_nodeSetUp(self):
        idx = self.node.getIdx()
        ip = self.node.getIp()

        self.assertEqual(idx,1)
        self.assertEqual(ip,"192.168.133.33")

    def test_SetTest(self):
        self.node.setIdx(2)

        self.assertEqual(self.node.getIdx(),2)

        self.node.setIp("192")

        self.assertEqual(self.node.getIp(),"192")

if __name__ == '__main__':
    unittest.main()


