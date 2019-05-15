import unittest
import sys
sys.path.insert(0, '../')
import config

class ConfigTest(unittest.TestCase):
    def listenPortTest(self):
        assertEqual(config.listenPort,8888)


if __name__ == '__main__':
    unittest.main()
