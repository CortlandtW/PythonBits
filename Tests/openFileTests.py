import unittest

import appStartLogging as log

#reload(unittest)
from testfixtures import LogCapture, compare


def displayNextTest(instance):
    print('=.'*15 + ' '*3 + instance._testMethodName + ' '*4 + '= '*19)

class MyTestOpen(unittest.TestCase):
# Tests of methods documented at:    https://pythonhosted.org/testfixtures/logging.html
    fileRef = '..\\Data\\TADdata1.csv'
    fileRefBad = '..\\Data\\doesnotexist.csv'
    msg1 = 'my log message - @#$@'

    def setUp(self):
        pass

    def test1_open(self):
        displayNextTest(self)
        with LogCapture() as cap:
            log.init_LogCapture()
            f = openFile.openFile(self.fileRefBad)
            print("File object <-- open non-existant-file:    %s" % type(f))
            print(cap)
            compare(cap.records[0].getMessage(),openFile.msg_CSVFileNotFound)
            self.assertIsNone(f,'Function must return None for this non-existent file.')
            #cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert

    def test2_openFileRef(self):
        displayNextTest(self)
        with LogCapture() as cap:
            log.init_LogCapture()
            f = openFile.openFile(self.fileRef)
                # print("File object:    %s" % type(f))
                # if isinstance(f,file):
                #     print('is file type')
            print(cap)
            self.assertIsInstance(f, file,'assertIsInstance file .')
            self.assertIs(type(f), file,'open() function must return file object when file exists.')
            #cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
            f.close()

    # from testfixtures import log_capture
    # @log_capture()
    # def test2_decorator(self):
    #     # only want to capture logging for the decorated test function
    #     cap = LogCapture()
    #     log.init_LogCapture()
    #     log.techl.info(self.msg1)
    #     #print(cap)
    #     cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
    #     cap.uninstall()       # required to avoid warning message
    #
    # def test3_manualUsage(self):
    #     cap = LogCapture()
    #     log.init_LogCapture()
    #     log.techl.info(self.msg1)
    #     #print(cap)
    #     cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
    #     cap.uninstall()        # required to avoid warning message
    # def tearDown(self):
    #     pass






if __name__ == '__main__':
    unittest.main()
    unittest

    # readTestSuite = unittest.TestSuite()
    # #readTestSuite.addTest(readCSVTest('test_default_size'))
    # readTestSuite.addTest(readCSVTest)

    # testsuite = unittest.TestLoader().discover('.')
    # unittest.TextTestRunner(verbosity=1).run(testsuite)