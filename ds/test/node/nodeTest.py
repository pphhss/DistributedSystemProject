import unittest
import sys
sys.path.insert(0,'../../../')
from ds.node import node,data

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = node.Node(1,"192.168.133.33")

    def test_nodeSetUp(self):
        idx = self.node.getIdx()
        ip = self.node.getIp()

        self.assertEqual(idx,1)
        self.assertEqual(ip,"192.168.133.33")

    def test_SetTest(self):
        self.node.setIdx(2)

        self.assertEqual(self.node.getIdx(),2)

        self.node.setIp("192")

        self.assertEqual(self.node.getIp(),"192")

    def test_setDatas(self):
        data1 = data.Data()
        data1.setKey(1)
        data1.setVersion(1)

        data2 = data.Data()
        data2.setKey(2)
        data2.setVersion(1)

        self.node.addData(data1)
        self.node.addData(data2)
        
        self.assertEqual(self.node.getData(1).getKey(),1)
        self.assertEqual(self.node.getData(2).getKey(),2)

if __name__ == '__main__':
    unittest.main()


