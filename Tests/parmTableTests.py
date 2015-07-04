import parmTable                 # the module under test

import unittest
import csv

from Tests import testutils_files
from testfixtures import LogCapture, compare
from apptestutils import displayNextTest

import appStartLogging as log
import appRoutines

unitTestMode = True

class readRowTests0(unittest.TestCase):
# Tests of methods documented at:    https://pythonhosted.org/testfixtures/logging.html
    fileRef = '..\\Data\\TADdata1.csv'
    fileRefBad = '..\\Data\\doesnotexist.csv'
    msg1 = 'my log message - @#$@'

    unitTestMode = True
    def setUp(self):
        pass

    def test0(self):
        displayNextTest(self)

        appRoutines.unitTestMode = True
        testutils_files.testx()
        with LogCapture() as cap:

            log.init_LogCapture()
            f = testutils_files.openCSVFile(self.fileRef)
            self.f = f
            self.assertIs(type(f), file,'open() function must return file object when file exists.')

            fd = csv.DictReader(f)
            print('- Column Headers:  %s' % fd.fieldnames)   # list of column header strings
            cap.clear()    # ignore previous logs
            self.assertTrue( set(parmTable.requiredColumnNames).issubset(fd.fieldnames),
                                msg='Required columns names missing.')
            row = next(fd)
            crow = parmTable.parmFileRec(row)
            print('row = %d  ID = "%s"' % (0, crow.id))
            #self.assertEqual(crow.url, row['ID'],msg='dict lookup and parmFileRec object agree on value')
            # same as assertEqual except displays the compared values on failure
            compare(crow.id, row['ID'],msg='dict lookup and parmFileRec object agree on value')

            print('Number of missing columns = %d  ' % crow.missingColumnsCnt)
            self.assertEqual('1', crow.id, msg='ID column does not contain correct value')
            print(cap)
            cap.check()    # no logs expected

    def tearDown(self):
        self.f.close()

#set([1, 2, 2]).issubset([1, 2])
# for i, row in enumerate(fd):   # iterate thru rows in fd with i as row counter
#     if i > 0: break
#     print('Line number %d' % fd.line_num)   # line 1 is column headers, 2 is first line of data
#     print(row)
#     crow = parmTable.parmFileRec(row)
#     print('row = %d  ID = "%s"' % (i, crow.id))
#     self.assertEqual(crow.id, row['ID'],msg='dict lookup and parmFileRec object agree on value')