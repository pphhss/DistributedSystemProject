import unittest
import sys
sys.path.insert(0, '../../../')
from ds.operation import operation



class AddParticipantTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_insert(self):
        res = operation.addParticipant("localhost")
        self.assertEqual(res, 1)

if __name__ == '__main__':
    unittest.main()
