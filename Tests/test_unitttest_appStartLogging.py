import appStartLogging as log
import unittest
from testfixtures import LogCapture, compare
import apptestutils


class unittest_LogCapture_tests(unittest.TestCase):
# Tests of methods documented at:    https://pythonhosted.org/testfixtures/logging.html

    msg1 = 'my log message - @#$@'
    def setUp(self):
        pass
    #         cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert


    def test1_withMethod(self):
        apptestutils.displayNextTest(self)
        # Demonstrate the logging data reported by the LogCapture.records methods.
        with LogCapture() as cap:
            log.init_LogCapture()
            log.techl.info(self.msg1)
            cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
            print('** Logs record as formatted by LogCapture')
            print(cap)

            log.techl.info('2nd log record')
            log.techl.info('3rd log record')
            self.assertEqual(len(cap.records),3,msg='len of records list = 3'
            #  Negative indexes count backwards - last item is at -1
            print('** cap.records[-2].getMessage = %s ' % cap.records[-2].getMessage()  )
            self.assertEqual(cap.records[0].getMessage(), self.msg1,
                             msg="Log message set not in log record")
            print('** cap.records[0].name = %s ' % cap.records[0].name)



    def test2_withMethod_userl(self):
        apptestutils.displayNextTest(self)
        # Demonstrate simple use of with LogCapture().
        with LogCapture() as cap:
            log.init_LogCapture()
            log.userl.info(self.msg1)
            print(cap)
            cap.check((log.userlName, 'INFO', self.msg1))     # a unittest assert

    from testfixtures import log_capture
    @log_capture()
    def test3_decorator_techl(self):
        # only want to capture logging for the decorated test function
        apptestutils.displayNextTest(self)
        cap = LogCapture()
        log.init_LogCapture()
        log.techl.info(self.msg1)
        #print(cap)
        cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
        cap.uninstall()       # required to avoid warning message

    def test4_manualUsage(self):
        apptestutils.displayNextTest(self)
        cap = LogCapture()
        log.init_LogCapture()
        log.techl.info(self.msg1)
        #print(cap)
        cap.check((log.techlName, 'INFO', self.msg1))     # a unittest assert
        cap.uninstall()        # required to avoid warning message

    def tearDown(self):
        pass






if __name__ == '__main__':
    unittest.main()
