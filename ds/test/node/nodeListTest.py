import unittest
import sys
sys.path.insert(0,'../../../')
from ds.node import nodeList,node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.nl = nodeList.NodeList
        pass

    def test_insertNode(self):
        self.nl.clear()
        self.nl.insertNode("192.168.133.3")
        self.assertEqual(self.nl.len(),1)

    def test_getNode(self):
        self.nl.clear()
        self.nl.insertNode("111")
        testNode = self.nl.getNode(0)
        self.assertEqual(testNode.getIp(),"111")

    def test_getNodeByIp(self):
        self.nl.clear()
        self.nl.insertNode("111")
        testNode = self.nl.getNodeByIp("111")
        self.assertEqual(testNode.getIp(),"111")

if __name__ == '__main__':
    unittest.main()

