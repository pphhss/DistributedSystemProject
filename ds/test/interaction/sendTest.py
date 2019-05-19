import unittest
import sys
sys.path.insert(0,'../../../')
from ds.interaction import send
from ds.node import nodeList

class sendTest(unittest.TestCase):

    def setUp(self):
        nodeList.NodeList.insertNode('localhost')

    def test_sendMessageToNode(self):
        res = send.SendManager.sendMessageToNode(0,"helloworld")
        self.assertEqual(res["result"],1)

if __name__ == '__main__':
    unittest.main()

