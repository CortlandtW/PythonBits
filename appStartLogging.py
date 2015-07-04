# appStartLogging
import CreateLogFileRef
import logging
import sys

# globals for module  - reference as  appStartLogging.techl
techl = None
userl = None
techlName = None
techlName = None



def setup_tech_log(normalrun=True):
    try:
        log = logging.getLogger(('app'))   # create logging object; logname = 'app'
        log.setLevel(logging.DEBUG)
        logFormat = logging.Formatter("%(asctime)s %(message)s")
        log.propagate = False

        if normalrun:
            logFileRef = CreateLogFileRef.initLogFile(".\\TechLogs")  # creates log file in path named
            file_hand = logging.FileHandler(logFileRef)    # assign handler to log file
            file_hand.setFormatter(logFormat)
            log.addHandler(file_hand)    # assign FileHandler
            return log
        else:          # unittesting
            stdlist_hand = logging.StreamHandler(sys.stdout)
            log.addHandler(stdlist_hand)
            #-log.propagate = False
            return log
    except:
        print("setup_tech_log  %s" % exObj)
        return None

def _generic_startLogFiles(normalRun):
    global techl
    global userl
    userl = setup_user_log(normalRun)
    if userl is None:
        print(exObj)
        sys.exit('Failure setting up user log')
    techl = setup_tech_log(normalRun)
    if techl is None:
        print(exObj)
        sys.exit('Failure setting up techl log')

def startLogFiles():
    """  1) Create log file name, 2) add path if required,
    3) create log file.
    Creates the file now to prevent conflicts.  Logger will connect with this file.
    Returns values in global variables  techLog & userl.
    These variables must be declared in the main module to make them global to the app.
    :return:  see global variables
    ABEND: Critical function; aborts if cannot open log files.
    """
    #global techLog
    global userl
    _generic_startLogFiles(True)


###############  unittests   ###################################
def startLogFiles_Stdout():     # not used except for routing log messages to stdout
    """
    """
    global techl
    global userl
    _generic_startLogFiles(False)
    return userl, techl

# For unit testing
def init_LogCapture():
    """ Use with unittesting using LogCapture from the textfixture library.
    """
    global techl
    global userl
    global techlName
    global userlName
    techlName = 'techl'
    userlName = 'userl'
    techl = logging.getLogger(techlName)   # create default logging object
    techl.setLevel(logging.DEBUG)
    userl = logging.getLogger(userlName)   # create default logging object
    userl.setLevel(logging.DEBUG)
    return userl, techl



if __name__ == '__main__':
    # Test - manually check that the 2 files exist & contain the right messages
    startLogFiles()
    userl.info("User Log info  - in normal use is also be logged to the techlog file.")
    techl.info("Tech log only info")


######################################################
# def setup_user_log(normalrun=True):
#     global exObj
#     try:
#         logFormat = logging.Formatter("%(asctime)s %(message)s")
#         log = logging.getLogger(('app.user'))   # create logging object; logname = 'app'
#         log.setLevel(logging.DEBUG)
#         log.propagate = True
#
#         if normalrun:
#             logFileRef = CreateLogFileRef.initLogFile(".\\UserLogs")  # creates log file in path named
#             file_hand = logging.FileHandler(logFileRef)    # assign handler to log file
#             file_hand.setFormatter(logFormat)
#             log.addHandler(file_hand)    # assign FileHandler
#             return log
#         else:
#             stdlist_hand = logging.StreamHandler(sys.stdout)
#             displayFormat = logging.Formatter("User Log: %(message)s")
#             stdlist_hand.setFormatter(displayFormat)
#             log.addHandler(stdlist_hand)
#             log.propagate = False
#             #
#
#             return log
#     except BaseException as exObj:
#         print("setup_user_log  %s" % exObj)
#         return None


# def _explore():
#     userLog = setup_user_log(True)
#     if userLog is None:
#         print(exObj)
#         sys.exit('Failure setting up user log')
#     techLog = setup_tech_log(True)
#     if techLog is None:
#         print(exObj)
#         sys.exit('Failure setting up techl log')
#     print(techLog.name)
#     #userl.error("serious error")
#     userLog.info("User Log info")
#     techLog.info("Tech log only info")