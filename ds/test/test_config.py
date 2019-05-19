import unittest
import sys
#sys.path.append("..")
from ds import config
#import config

class ConfigTest(unittest.TestCase):
    def test_listenPort(self):
        self.assertEqual(config.listenPort,8888)


if __name__ == '__main__':
    unittest.main()
