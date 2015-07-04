#Logging HOWTO          https://docs.python.org/2/howto/logging.html
#Logging Cookbook       https://docs.python.org/2/howto/logging-cookbook.html#

Good reference on using logging's own buffer handler for searching on log entries
# http://plumberjack.blogspot.com/2010/09/unit-testing-and-logging.html

import unittest
import cStringIO
import logging
import sys

h1 = logging.StreamHandler(sys.stdout)

rootLogger = logging.getLogger()
rootLogger.addHandler(h1)
logger = logging.getLogger("my.logger")
logger.setLevel(logging.DEBUG)
logger.info("my message to log")


#if __name__ == '__main__':
#    unittest.main()




# class MyTest(unittest.TestCase):
#     def setUp(self):
#
#
#     def testLog(self):
#
#         print '[', self.stream.getvalue(), ']'
#         self.assertTrue(self.stream.getvalue(), 'test')
#
#     def tearDown(self):
#         self.log.removeHandler(self.handler)
#         self.handler.close()
