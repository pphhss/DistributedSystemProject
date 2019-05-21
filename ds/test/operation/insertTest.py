import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.interaction import send
from ds.node import nodeList

class InsertLocalTest(unittest.TestCase):

    def setUp(self):
        nodeList.NodeList.insertNode('localhost')

    def test_sendMessageToNode(self):
        res = send.SendManager.sendOperationToNode(0,"insert","nicetomeetyou")
        print("test_sendMessageToNode response result : ",res["result"])
        self.assertEqual(res["result"],1)
if __name__ == '__main__':
    unittest.main()

