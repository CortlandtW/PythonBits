#from inspect import stack
#import sys
import csv

import appStartLogging as log
import appRoutines


logMsg0 = 'Testing only**'
logMsg1 = 'Error opening parameter file: '
logMsg2_openedParmFile = 'Opened parameter file: '

class ReadCSVFile(object):
    def __init__(self):
        self.isOK = True
        #self.isError = False

    def open(self, fileRef):
        """ Open :fileRef: with read mode.
        When successful creates csvFileObj (internal reference to opened file)
        """
        def _attemptingMsg():
            log.userl.critical(
                'ERROR while Attempting to open parameter file: %s' % fileRef)
        #----------------------------------------------------

        self.csvFileRef = fileRef
        self.isOK = False
        try:
            self.csvFileObj = open(fileRef, 'rb')
        except ValueError as exArg:
            _attemptingMsg()
            log.userl.critical('ValueError:  %s' % exArg)
            appRoutines.appABEND()     # abort program
        except IOError as exArg:
            _attemptingMsg()
            log.userl.critical('IOError:  %s' % exArg)
            appRoutines.appABEND()     # abort program
        except Exception, exArg:
            _attemptingMsg()
            log.userl.critical('Unexpected error type encountered: %s' % exArg)
            appRoutines.appABEND()     # abort program
        else:
            self.isOK = True
            log.userl.info('%s %s' % (logMsg2_openedParmFile, fileRef))   # Opened parameter file:

    def dictReader(self):
        ''' Read entire csv file to 'dictionary reader object'.
        The object is somewhat similar to an array of dictionaries, 1 dict per row
        '''
        self.isError = True
        self.fileAsDict = None
        try:
            dictReaderObj = csv.DictReader(self.csvFileObj, delimiter=',', quotechar='"')
        except Exception, exArg:
            print "Exception type = " + type(exArg)
            log.userl.critical(
                'ERROR while Attempting to read CSV formatted parameter file: %s' % fileRef)
            log.userl.critical('read CSV error: %s' % exArg)
            appRoutines.appABEND()     # abort program
        else:
            self.isError = False

        self.dictReaderObj = dictReaderObj
        return dictReaderObj


        # exception block
        #     print(sys.exc_value)    # 'Illegal characters in path.'
        #     print(sys.exc_type)     # <type 'exceptions.ValueError'>
        #     print(sys.exc_info())    # both above + <traceback ...
# if __name__ == '__main__':
#    unittest.main()

            #print 'IOError msgs'
            #print str(exArg.message)
            #print '.args = ' + str(exArg.args)
            #print exArg.errno
            #print exArg.strerror