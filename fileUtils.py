import appStartLogging as log
"""
Common file oriented functions
"""

def openFileOrLog(fileRef, noOpenLog, noOpenMsg, mode='r'):
    """
    :param fileRef - file reference including path and file name
        of file to open;  f = open(fileRef, mode).
    :param noOpenLog - Reference to Python object log instance.logname.level
        which shall write/log the noOpenMsg if fileRef cannot be opened.
        Example: log.userl.critical
    :param noOpenMsg  - method  from appStartLogging
            e.g. log.user.critical
    :return: f, file object; None = file not opened
    """
    try:
        f = open(fileRef, mode)
    except Exception, eArgs:
        noOpenLog(noOpenMsg)
        noOpenLog(eArgs)
        return None

    return f


