import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.interaction import send
from ds.node import nodeList
from ds import config

class InsertLocalTest(unittest.TestCase):
    
    def setUp(self):
        self.ip=config.ip
        nodeList.NodeList.insertNode(self.ip)

    def test_sendMessageToNode(self):
        res = send.SendManager.sendOperationToNode(0,"insert","test","nicetomeetyou")
        print("test_sendMessageToNode response result : ",res["result"])
        self.assertEqual(res["result"],1)
        self.assertIsNotNone(res["source"],self.ip)
if __name__ == '__main__':
    unittest.main()

