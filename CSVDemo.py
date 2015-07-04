# Old - newer version is GetCSF.py
import csv
import unittest
import cStringIO


class ReadCSVFile(object):
    csvFileRef = "C:\Users\Cortlandt\Documents\TAD\TAD_PythonDemoBits\DSADist.csv"

    logMsgs_CSV = {'test':'Ttesting only**', \
                1:'Error opening parameter file: ', \
                5:'CSV file opened'}
    global log
    def __init__(self):
        self.isOK = True
        self.isError = False

    def open(self, fileRef):
        try:
            self.csvFileObj = open(fileRef, 'rb')
        except IOError, exArg:
            common_exception(exArg.strerror)
        except Exception, exArg:
            print "Exception type = " + str(type(exArg))
            common_exception(exArg)
        else:
            self.isError = False
            # make log entry when columns verified

    def read(self):
        ''' Read entire csv file to buffer (an array of dictionaries, 1 dict per row '''
        self.isError = True
        try:
            cFile = csv.DictReader(self.csvFileObj, delimiter=',', quotechar='"')
        except Exception, exArg:
            print "error DictReader"
            print "Exception type = " + type(exArg)
            print str(exArg)
        else:
            self.isError = False
            print "DictReader results"
            print type(cFile)
            line = cFile.fieldnames
            print line
        self.cFile = cFile      


class CSVFileTests(unittest.TestCase):
    # constants
    def setUp(self):
        global log
        log = cStringIO.StringIO()     # write to stream instead of disc file
        self.f = ReadCSVFile()
        self.log = log

    def tearDown(self):
        self.f = None
        self.log = None

    def test_log_with_StringIO(self):
        ''' Log 'fake' - Open, write & verify log file contents '''
        self.log.write("This is a ttest")
        contents = self.log.getvalue()
        self.assertIn("a ttest",contents)
        
    def test_init(self):
        ''' Test of  _init_ method (basic) '''
        #f = ReadCSVFile()
        contents = self.log.getvalue()
        self.assertIn(ReadCSVFile.logMsgs_CSV['test'],contents,"Test of log entry")
        self.assertEqual(self.f.isError,False,"Test of status flag")

    def test_open_file_exists(self):
        ''' Open file - file should exist & open succeed '''
        self.f.open(ReadCSVFile.csvFileRef)
        self.assertEquals(self.f.isOK,True,"Open method-file should exist & open succeed")
        contents = self.log.getvalue()
        #print 'Successful open msg = ', contents   gets everything in file
        
    def test_open_file_notExists(self):
        ''' Open dummy file - method should return error & error msg on log'''
        self.f.open("C:\Users\dummy.csv") 
        self.assertEquals(self.f.isError,True,"Open method-dummy file, should return error")
        contents = self.log.getvalue()
        self.assertIn(ReadCSVFile.logMsgs_CSV[1],contents,"Open method-dummy file, should write log entry for error") 

    def test_DictReader(self):
        ''' Use csv.DictReader to read and parse entire file into a list of dicts '''
        self.test_open_file_exists()   # open the file using previous test case
        self.assertEquals(self.f.isError,False,"read() method-open succeed")
        self.f.read()
        #print type(self.f.cFile)
        r = self.f.cFile.next()
        #print r['ID']
        self.assertEqual(r['ID'],'1','Read 1st row, ID column = ')

        #self.assertIsInstance(self.f.cFile,list,'read() method should return a list of dicts')
        

if __name__ == '__main__':
   unittest.main()

            #print 'IOError msgs'
            #print str(exArg.message)
            #print '.args = ' + str(exArg.args)
            #print exArg.errno
            #print exArg.strerror