__author__ = 'Cortlandt'
#+++++++++++++++++++++++++++++++++++++++++++++
Module: SimpleFile
class SimpleFile(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def write_text(self, textToWrite):
        f = open(self.fileName, 'w')
        f.write(textToWrite)
        f.close()

    def read_text(self):
        f = open(self.fileName, 'r')
        read = f.read()
        return read
#---------------------
import unittest
import os
from files.core import SimpleFile

class Test(unittest.TestCase):

    def get_file_name(self):
        fileName = "bar.txt"
        return fileName

    def get_file_text(self):
        textToWrite = "This line"
        return textToWrite

    def test_write_file(self):
        simple_file = SimpleFile(self.get_file_name())
        simple_file.write_text(self.get_file_text())
        self.assertTrue(os.path.isfile(self.get_file_name()))

    def test_read_file(self):
        simple_file = SimpleFile(self.get_file_name())
        read_text = simple_file.read_text()
        self.assertEqual(read_text,self.get_file_text())
#===========================================================
#######################################################################################
def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

##########################################################################################

# To avoid using a real file  separate the creation of a stream from writing to / reading from the stream

def readInitialsFromFileStream(fileStream):
    return fileStream.readline()

...
def testReadingOfInitialsFromFileStream():
    testStream = io.StringIO()
    testStream.write('T.M.')
    testStream.seek(0)
    assert('T.M.', readInitialsFromFileStream(testStream))
###############################################################
utils_logger.error.assert_called_with(
            SubstringMatcher(containing='wrong currency'))

from string import lower
class SubstringMatcher():
    def __init__(self, containing):
        self.containing = lower(containing)
    def __eq__(self, other):
        return lower(other).find(self.containing) > -1
    def __unicode__(self):
        return 'a string containing "%s"' % self.containing
    def __str__(self):
        return unicode(self).encode('utf-8')
    __repr__=__unicode__


TestFixtures documentation     https://pythonhosted.org/testfixtures/index.html

TestFixtures is a collection of helpers and mock objects that are useful when writing unit tests.