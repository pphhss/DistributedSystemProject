import unittest
import sys
sys.path.insert(0, '../../../')
from ds.node import nodeList
from ds.externalOperation import externalOperation as exop
from ds import config

class ExternalInsertTest(unittest.TestCase):

    def setUp(self):
        self.key = "exopInsertTest5"
        nodeList.NodeList.insertNode(config.ip)
        pass

    def test_isWorkInNodeList(self):
        res = exop.insert(self.key, "hi")
        print(res)
        self.assertEqual(nodeList.NodeList.isMe(self.key), True)
        self.assertEqual(res["success"], 1)
        self.assertEqual(res["fail"], 0)


if __name__ == '__main__':
    unittest.main()
