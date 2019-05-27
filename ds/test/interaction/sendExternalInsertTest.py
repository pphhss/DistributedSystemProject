import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.node import nodeList
from ds.interaction import send
from ds import config


class SendExternalInsertTest(unittest.TestCase):
    
    def setUp(self):
        self.ip=config.ip
        nodeList.NodeList.insertNode(self.ip)

    def test_SendExternalInsertTest(self):
        mes = {}
        mes["opcode"] = "insert"
        mes["key"] = "eiTEST2"
        mes["value"] = "aa"
        res = send.SendManager.sendExternal(self.ip,mes)
        print("test_sendMessageToNode response result : ",res)
        self.assertEqual(res["result"],1)
if __name__ == '__main__':
    unittest.main()

