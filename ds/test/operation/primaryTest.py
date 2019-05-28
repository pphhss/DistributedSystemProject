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

if __name__ == '__main__':
    unittest.main()
