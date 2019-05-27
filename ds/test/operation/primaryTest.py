import unittest
import sys
sys.path.insert(0, '../../../')
from ds import config
from ds.node import nodeList
from ds.operation import operation


class OperationTest(unittest.TestCase):

    def setUp(self):
        self.ip = config.ip
        nodeList.NodeList.insertNode(self.ip)
        self.key = "primaryTest1"

    def test_operationPrimary(self):
        res = operation.primary(self.ip, self.key, "11")
        self.assertGreaterEqual(res,0)
        targetNode = nodeList.NodeList.getNodeByIp(self.ip)
        self.assertEqual(targetNode.getData(self.key).getKey(), self.key)


if __name__ == '__main__':
    unittest.main()
