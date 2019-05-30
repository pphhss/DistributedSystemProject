import unittest
import sys
sys.path.insert(0, '../../../')
from ds.node import nodeList
from ds.externalOperation import externalOperation as exop
from ds import config

class ExternalUpdateTest(unittest.TestCase):

    def setUp(self):
        self.key = "primaryTest6"
        #nodeList.NodeList.insertNode(config.ip)
        pass

    @unittest.skip("test_primary skipping")
    def test_updatea_if_i_am_primary(self):
        nodeList.NodeList.insertMe(self.key,0)
        res = exop.update(self.key, "hi")
        print(res)
        self.assertEqual(nodeList.NodeList.isMe(self.key), True)
        self.assertEqual(res["success"], 1)
        self.assertEqual(res["fail"], 0)
    

    def test_update_if_i_am_not_primary(self):
        nodeList.NodeList.insertNode(config.ip)
        nodeList.NodeList.insertDataInNode(config.ip,self.key)
        res=exop.update(self.key,"good")
        print(res)
        self.assertEqual(res["success"],2)
        
        


if __name__ == '__main__':
    unittest.main()
