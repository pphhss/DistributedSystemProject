import unittest
import sys
sys.path.insert(0,'../../../')
from ds.node import nodeList,node

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.nl = nodeList.NodeList
        pass

    def test_insertNode(self):
        self.nl.clear()
        self.nl.insertNode("192.168.133.3")
        self.assertEqual(self.nl.len(),1)

    def test_getNode(self):
        self.nl.clear()
        self.nl.insertNode("111")
        testNode = self.nl.getNode(0)
        self.assertEqual(testNode.getIp(),"111")

    def test_getNodeByIp(self):
        self.nl.clear()
        self.nl.insertNode("111")
        testNode = self.nl.getNodeByIp("111")
        self.assertEqual(testNode.getIp(),"111")

    def test_getMe(self):
        self.nl.clear()
        me = self.nl.getMe()
        self.assertIsNotNone(me)

    def test_isMe(self):
        self.nl.clear()
        self.nl.insertMe("isMeTest",0)
        res1=self.nl.isMe("isMeTest")
        res2 = self.nl.isMe("isMeTest1")
        self.assertEqual(res1,True)
        self.assertEqual(res2,False)

    def test_getVersion(self):
        key = "getVersionTest"
        self.nl.clear()
        self.nl.insertMe(key,0)
        self.assertEqual(self.nl.getVersionInMe(key),0)

    def test_updateVersion(self):
        key = "getVersionTest"
        self.nl.clear()
        self.nl.insertMe(key,0)
        self.nl.updateVersion(key,1)
        self.assertEqual(self.nl.getVersionInMe(key),1)

    def test_getVersionInOther(self):
        self.nl.clear()
        self.nl.insertNode("ff")
        self.nl.insertDataInNode("ff","key")
        self.assertEqual(self.nl.getVersionInOtherNode("key"),0)

    def test_updateNewPrimary(self):
        key="key"
        n1 = "n1"
        n2 = "n2"
        
        self.nl.clear()
        self.nl.insertNode(n1)
        self.nl.insertNode(n2)
        self.nl.insertDataInNode(n1,key)
        self.nl.updateNewPrimary(key,1,n2)

        self.assertEqual(self.nl.getVersionInOtherNode(key),1)


if __name__ == '__main__':
    unittest.main()

