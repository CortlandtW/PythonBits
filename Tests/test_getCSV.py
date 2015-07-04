import getCSV    # module tested

import unittest
from Tests import testfixtures2 as tfix
from Tests import apptestutils

import os
import re

import appStartLogging as log
import appRoutines
import appData

import csv

appData.runMode = appData.RUNMODE_TEST

#csvFileRef = "C:\Users\Cortlandt\Documents\TAD\TAD_PythonDemoBits\DSADist.csv"
csvFileRef = "..\Data\DSADist.csv"
badFileRef  = "C:\Users\Cortlandt\Documents\TAD\TAD_PythonDemoBits\Data\nosuchfileexists.csv"

class CSVFileTests(unittest.TestCase):

    def common(cls):
        apptestutils.displayNextTest(cls)
        log.init_LogCapture()       # start logging for unit testing
        appData.runMode = appData.RUNMODE_TEST

    def test0_openNoSuchFile(self):
        ''' Open non-existing file.
        Should trigger appRoutines.appABEND which in turn
        issues log message appRoutines.abendMsg1. '''
        self.common()
        with tfix.LogCapture() as cap:
            r = getCSV.ReadCSVFile()
            r.open(badFileRef)
            lastREx = ''.join(['^', appRoutines.abendMsg1,'.*$'])
            #print('Regular Expression: %s' % lastREx)
            #  -1 is index for last item - offset from len(cap.records).
            tfix.compare( tfix.StringComparison(lastREx), cap.records[-1].getMessage() )
            #       string comp     without RegEx
            #self.assertEqual(cap.records[-1].getMessage(), appRoutines.abendMsg1,
            #                 msg="Last log rec should be ABEND final message.")
            print(cap)

    def test1_openExistingFile(self):
        ''' Test of  _init_ method (basic) '''
        self.common()

        with tfix.LogCapture() as cap:
            r = getCSV.ReadCSVFile()
            r.open(csvFileRef)
            print(os.path.abspath(csvFileRef))
            log.userl.info('dummy message')
            print(cap)
            # non RegEx method of running test assuming we know the log index
            self.assertIn('Opened',cap.records[0].getMessage(),
                      "Test of log entry")

            msg = '%s.*%s' % (getCSV.logMsg2_openedParmFile,re.escape(csvFileRef))
            rowIndex, msgFound = cap.findLog(cap,'*','*', msg, msgRegEx=True, display=True)
            self.assertIsNotNone(msgFound,
                 msg="Did not find 'Opened parameter file' message in log")
            if rowIndex is not None:    # redundant with the display=True parm above
                print('Found in row %i is the text %s' % (rowIndex, msgFound))


    def test2_read(self):
        self.common()
        with tfix.LogCapture() as cap:
            r = getCSV.ReadCSVFile()
            r.open(csvFileRef)
            dictReaderObj =  r.dictReader()

            row = dictReaderObj.next()     # NEXT in interator object

            self.assertEqual(row['ID'],'1',msg='Read ID in 1st row')

            print(row)
            print('--------')
            print(dictReaderObj.fieldnames)
            #------ other stuff that works

            self.assertTrue("URL" in row,msg="URL column header not found")  # find 1 column name
            headers = ['ID', 'URL']   # find set of column names
            self.assertTrue(set(headers).issubset(dictReaderObj.fieldnames),
                msg="Subset operation failed")

            print("\r\nx in row/dictReader interator object")
            for col in row:
                print(' -- %s ==> %s' %  (col, row[col]))
            for col in headers:
                self.assertTrue(col in dictReaderObj.fieldnames)  # tautology
            #----------------------------
            row = dictReaderObj.next()  # NEXT in interator object
            #print("\r\nNext x in row/dictReader interator object")


11
12
13
14
15
16
17
18
19
20
21

# #compare two lists and print the differences
#
# #opens first file to compare
# with open("file1.txt") as file1list:
#         file1l = file1list.read().splitlines()
#
# #opens second file to compare
# with open("file2.txt") as file2list:
#         file21 = file2list.read().splitlines()
#
# #assigns files to sets
# set1=file1l
# set2=file2l
# ---------------------------


#
# #Prints everything in set b that's not in set a
# def difference(a, b):
#     return list(set(b).difference(set(a)))
#
# list_diff=difference(set1,set2)
#
# print list_diff




# class CSVFileTests(unittest.TestCase):
#     # constants
#     def setUp(self):
#         global log
#         log = cStringIO.StringIO()     # write to stream instead of disc file
#         self.f = ReadCSVFile()
#         self.log = log
#
#     def tearDown(self):
#         self.f = None
#         self.log = None
#
#     def test_log_with_StringIO(self):
#         ''' Log 'fake' - Open, write & verify log file contents '''
#         self.log.write("This is a ttest")
#         contents = self.log.getvalue()
#         self.assertIn("a ttest",contents)
#
#     def test_init(self):
#         ''' Test of  _init_ method (basic) '''
#         #f = ReadCSVFile()
#         contents = self.log.getvalue()
#         self.assertIn(ReadCSVFile.logMsgs_CSV['test'],contents,"Test of log entry")
#         self.assertEqual(self.f.isError,False,"Test of status flag")
#
#     def test_open_file_exists(self):
#         ''' Open file - file should exist & open succeed '''
#         self.f.open(ReadCSVFile.csvFileRef)
#         self.assertEquals(self.f.isOK,True,"Open method-file should exist & open succeed")
#         contents = self.log.getvalue()
#         #print 'Successful open msg = ', contents   gets everything in file
#
#     def test_open_file_notExists(self):
#         ''' Open dummy file - method should return error & error msg on log'''
#         self.f.open("C:\Users\dummy.csv")
#         self.assertEquals(self.f.isError,True,"Open method-dummy file, should return error")
#         contents = self.log.getvalue()
#         self.assertIn(ReadCSVFile.logMsgs_CSV[1],contents,"Open method-dummy file, should write log entry for error")
#
#     def test_DictReader(self):
#         ''' Use csv.DictReader to read and parse entire file into a list of dicts '''
#         self.test_open_file_exists()   # open the file using previous test case
#         self.assertEquals(self.f.isError,False,"read() method-open succeed")
#         self.f.read()
#         #print type(self.f.cFile)
#         r = self.f.cFile.next()
#         #print r['ID']
#         self.assertEqual(r['ID'],'1','Read 1st row, ID column = ')
#
#         #self.assertIsInstance(self.f.cFile,list,'read

# def ext_testSetUp():
#     apptestutils.bannerMsg('testSetUp')
#     log.init_LogCapture()       # start logging for unit testing
#
# def raise_failureException():
#     msg = 'hi mom'
#     raise unittest.TestCase.failureException(msg)