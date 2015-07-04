import sys
import appData
import appStartLogging as log

abendMsg1 = 'Program ending with serious errors.'


def appABEND():
    """
    TESTING NOTE: To avoid sys.exit & a true ABEND
      SET  appData.runMode = appData.RUNMODE_TEST
    """
    print('appABEND')
    log.userl.critical('Program ending with serious errors.')
    if appData.runMode == appData.RUNMODE_NORMAL:
        sys.exit('Abnormal End of Process.')





