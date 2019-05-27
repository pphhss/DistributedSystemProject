import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.node import nodeList
from ds.interaction import send
from ds import config


class OperationTest(unittest.TestCase):
    
    def setUp(self):
        self.ip=config.ip
        nodeList.NodeList.insertNode(self.ip)

    def test_sendPrimaryToNode(self):
        res = send.SendManager.sendPrimaryToAllNode("primaryTest5","nicetomeetyoau")
        print("test_sendMessageToNode response result : ",res)
        self.assertEqual(res["success"],1)
        self.assertIsNotNone(res["fail"],0)
if __name__ == '__main__':
    unittest.main()

