""" Utilities for testing.
"""
import cStringIO
import os

def bannerMsg(msg="put your message here"):
    """  Banner line to display between unit tests.
    """
    print('=.'*5 + ' '*3 + msg + ' '*4 + '=.'*5)
def displayNextTest(self):
    """  Banner line to display between unit tests.  Shows the name of the method (def).
    """
    bannerMsg(self._testMethodName)
    #print('=.'*5 + ' '*3 + self._testMethodName + ' '*4 + '=.'*5)


def removeSilent(fileref_p):
    """ Deletes a file.
    :param fileref_p:  - reference to file to delete
    :return: True when file removed OK
    """
    try:
        os.remove(fileref_p)
    except OSError, e:
        # WindowsError: [Errno 2] The file could not be found for deletion: .\LogX.txt
        #print("e.errno = %s" % e.errno)
        if e.errno == 2:  return
        else: raise

def rmdirSilent(dirname_p):
    """ Deletes one directory.   1 level only.
    :param fileref_p:  - reference to file to delete
    :return: True when file removed OK
    """
    try:
        os.rmdir(dirname_p)
    except OSError, e:
        # WindowsError: [Errno 2] The file could not be found for deletion: .\LogX.txt
        print("rmdirSilent()  %s  e.errno = %s  %s" % (dirname_p, e.errno, e.strerror))
        if e.errno == 2:  return   # Could not find a part of the path
        else: raise

if __name__ == '__main__':
    #   removeSilent("LogX.txt")
    rmdirSilent(".\\testOnlynewDir")
    pass
