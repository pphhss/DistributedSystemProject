import unittest
import sys
sys.path.insert(0,'../../../')
from ds.operation import operation
from ds.interaction import send
from ds.node import participate
from ds import config

class participateTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_sendParticipate(self):
        res = participate.participate()
        self.assertEqual(res,1)
if __name__ == '__main__':
    unittest.main()

