import unittest
import sys
sys.path.insert(0, '../../../')
from ds import config
from ds.node import nodeList
from ds.operation import remoteWrite as rw
from ds.db import data


class RemoteWriteTest(unittest.TestCase):

    def setUp(self):
        self.ip = config.ip
        nodeList.NodeList.insertNode(self.ip)
        self.key = "primaryTest6"

    @unittest.skip("test_primary skipping")
    def test_primary(self):
        res = rw.primary(self.ip, self.key, "11")
        self.assertGreaterEqual(res,0)
        targetNode = nodeList.NodeList.getNodeByIp(self.ip)
        self.assertEqual(targetNode.getData(self.key).getKey(), self.key)

    def test_update(self):
        value = "13"
        res = rw.update(self.key,value,self.ip)
        self.assertIsNotNone(res)
        result = data.getDataFromKey(self.key)
        self.assertEqual(result["v"],value)

    def test_update_if_i_am_primary(self):
        value = "14"
        res = rw.update(self.key,value,self.ip)
        self.assertIsNotNone(res)
        result = data.getDataFromKey(self.key)
        self.assertEqual(result["v"],value)
if __name__ == '__main__':
    unittest.main()
