"""
Customized version of the textfixture module using inheritance.
"""

import re
from testfixtures.comparison import *
import testfixtures as testfixtures_lib



class LogCapture(testfixtures_lib.LogCapture):
    def wildThing(self):
        print("Running the app's customized version of the testfixtures module.")


    """  Find log message captured by testfixture2.LogCapture.
    Searches by log name, log level, and message with an
    option to search using regular expressions.
    Default for name and level is wildcard.
    :param LogCapture_self  instance of LogCapture
    :return A tuple - i, text
       Returns text = None when search fails.
       Where:
       i =  index of message captured by LogCapture
                and returned by the .actual method.
       text = Message string found or None if search failed.

    USAGE:
    Example 1:
        # Tested code should issue a log message ending with xxxFileRef.
        import testfixtures2 as tfix
        log.init_LogCapture()       # start logging for unit testing
        with tfix.LogCapture() as cap:
            ...
            msg = '%s.*%s' % ('some string',re.escape(xxxFileRef))
            rowIndex, msgFound = cap.findLog(cap,'*','*', msg, msgRegEx=True, display=True)
            self.assertIsNotNone(msgFound,
                 msg="Did not find 'Opened parameter file' message in log")
            if rowIndex is not None:    # redundant with the display=True parm above
                print('Found in row %i is the text %s' % (rowIndex, msgFound))
    Example 2:
        # Setup similar to above
        # Code under tests writes log.userl.critical("critical message")
        rowIndex, msgFound =  cap.findLog(
                cap, 'userl', 'CRITICAL', "critical message")
        self.assertIsNotNone(msgFound)
    """
    def findLog(self, LogCapture_self, name='*', level='*', msg='', msgRegEx=False, display=False):
        self.logFound = ()
        if msgRegEx:
            if isinstance(msg, basestring):
                expected_regexp = re.compile(msg)
            else:
                print('findLog function: illegal characters in RegEx string.')
        # iterate thru records in LogCapture with i as row counter
        # Each record is a 3 element list - log name, level (INFO,CRITICAL, etc), message
        for i, row in enumerate(LogCapture_self.actual()):
            if (not name == '*') and (not row[0] == name):
                continue
            if (not level == '*') and (not row[1] == level):
                continue
            text = row[2]   # text of message is 3rd element
            if msgRegEx:
                if expected_regexp.search(text):
                    return i, text
            else:
                if text == msg:
                    if row is not None:
                        if display:
                            print('Found in log %i of captured logs:' % i)
                            print(row)
                    self.logFound = row
                    return i, text
        if display:
            print('findLog function: Search on %s, %s, "%s" -- no hits' % (str(name), str(level), msg))
        return None, None

    def displayCapturedLogs(self, LogCapture_self, verbose=False):
        """
        Prints all logs captured by LogCapture as saved in the .actual method.
        """
        if verbose:
            print('Log messages captured:')
        for i, row in enumerate(LogCapture_self.actual()):
            if verbose:
                print('   %i: %s' % (i, row))
            else:
                print(row)
            #print(%s, %s, "%s" -- no hits' % (str(name), str(level), msg)
        if verbose: print('')