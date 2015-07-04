import fileUtils     # module to test

import unittest
from Tests import testfixtures2 as tfix
from Tests import apptestutils

import appStartLogging as log
import appData

errorMsg = 'bad file, cannot open'

class CSVFileTests(unittest.TestCase):

    def common(cls):
        apptestutils.displayNextTest(cls)
        log.init_LogCapture()       # start logging for unit testing
        appData.runMode = appData.RUNMODE_TEST

    def test1_openNoSuchFile(self):
        self.common()
        with tfix.LogCapture() as cap:
            f = fileUtils.openFileOrLog('nosuchfile',log.userl.critical,errorMsg)
            self.assertIsNone(f,msg='Should return None when cannot open file')
            cap.displayCapturedLogs(cap,verbose=True)
            rowIndex, msgFound =  cap.findLog(
                cap, 'userl', 'CRITICAL', errorMsg, msgRegEx=False, display=True)
            # print(cap.rowFound)
            self.assertIsNotNone(msgFound,
                                 msg="Did not find expected error message in log")


