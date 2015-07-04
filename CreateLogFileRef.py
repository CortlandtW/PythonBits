from time import  localtime, strftime
import sys
#++import os.path
from Tests import apptestutils

timeStamp = None

def _makeDateTimeStr():
    """ Returns a formatted date-timestamp string legal for use as a Windows file name.
    """
    dateTimeStr = strftime("%Y-%d-%d@%H-%M-%S", localtime() )
    assert isinstance(dateTimeStr, str)
    return dateTimeStr

def _makeTimeStamp():
    """ Make one time stamp at the beginning of a run and re-use;
    make all the time stamps for run the same.
    """
    global timeStamp
    if timeStamp is None:
        timeStamp = _makeDateTimeStr()
        return timeStamp
    else:
        return timeStamp

def makeDirSilent(path_p):
    """Try to create the directory or directories, but if they already exist we ignore the error.
    Equivalent to 'exist_ok=True' option in Python 3.2+:   os.makedirs(path, exist_ok=True)
    Also validates that the path is really a directory & not a file.
    This logic should avoid race conditions with other nearly simultaneous processes.
    Python NOTE: Back slashes must be doubled due to Python's string interpretation rules.
    Win NOTE: The .\ format indicates the current directory.
    >>>smartMakeDir(".\\Logs\\")
    True
    """
    try:
        os.makedirs(path_p)
        return True
    except OSError:
        if os.path.isdir(path_p):
            return True
        else:
            raise  # path is a file, not a directory!
            return False

def openFile(fileRef_p):
    try:
        f = open(fileRef_p, mode='w')     # Open mode = 'w' (write) overwrites an existing file
        return f
    except exception as e:
        print e
        #  sys.exit('exit - error opening file ' + fileRef_p)
        return None
###########################################################

def initLogFile(path='.\\UserLogs'):
    if not makeDirSilent(path):
        sys.exit('exit - error with path function creating log file')
    fn = 'Log_' + _makeTimeStamp() + ".txt"
    fileRef = path + '\\' + fn     # use double back slash in python literals
    f = openFile(fileRef)
    print("Log File created: %s" % fileRef)
    return fileRef


def _ExampleOfUse():
    #print(makeDateTimeStr())
    fn = 'Log_' + makeDateTimeStr()
    relPath = ".\\Logs\\"

    if not makeDirSilent(relPath):
        sys.exit('exit - error with path function')
    fileRef = relPath + fn

    f = openFile(fileRef)
    print(dir(f))
    print(type(f))
    print("File created: %s" % fileRef)

import os


def _xxx():
    fn = ".\\testfile.txt"
    apptestutils.removeSilent(fn)


#from apptestutils import removeSilent
import unittest
class test_FileOps(unittest.TestCase):

    def xremoveSilent(self, fileref_p):
        try:
            os.remove(fileref_p)
        except OSError, e:
            # WindowsError: [Errno 2] The file could not be found for deletion: .\LogX.txt
            #print("e.errno = %s" % e.errno)
            if e.errno == 2:  return
            else: raise

    def setUp(self):
        self.fn1 = ".\\testOnlyfile.txt"
        self.fn2 = ".\\dummyfile.txt"
        self.path1 = ".\\testOnlynewDir"
        #assert os.remove(self.fn1)
    def tearDown(self):
        pass

    def test1_openFile(self):
        # Test the openFile function
        apptestutils.removeSilent(self.fn1)   # delete file from os file system
        self.assertFalse(os.path.exists(self.fn1),msg="Verify: file must not exist")
        f = openFile(self.fn1)
        print(type(f))
        #self.assertEquals(type(f),<type 'file'>)
        #self.assertIs(type(f),'file')
        self.assertTrue(os.path.exists(self.fn1),msg="Just created file does exist")

    def test2_makeDirSilent(self):
        # Test the makeDirSilent function
        #   Does not test the 'silent mode' -- if messages are created
        apptestutils.rmdirSilent(self.path1)
        self.assertFalse(os.path.exists(self.path1),msg="Verify: path/directory must not exist")
        self.assertTrue(makeDirSilent(self.path1))
        self.assertTrue(os.path.exists(self.path1),msg="Verify: path/directory must not exist")

if __name__ == '__main__':
     #unittest.main()
     #_ExampleOfUse()
     initLogFile()