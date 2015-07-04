import appStartLogging as log
import csv
# Example  fileRef = '..\\Data\\TADdata1.csv'   step back one directory level then to dir named \Data

import appRoutines

def testx():
    appRoutines.appABEND()

msg_CSVFileNotFound = 'CSV File not found!   Process cannot continue without this file and must shut down.'
def openCSVFile(fileRef):
    """
    :param fileRef - file reference including path and file name.
    :return: f, file object; None = file not opened
    """
    try:
        f = open(fileRef, 'r')
    except Exception, eArgs:
        log.userl.critical(msg_CSVFileNotFound)
        log.userl.critical(eArgs)
        return None

    log.userl.info('CSV file containing parameters opened. -- %s' % f.name)  # f.name is relative fileref
    return f
    #f.close()

def CSVReader(f):
    fd = csv.DictReader(f)
    print(fd[0])







# if os.path.exists(fileRef):
    #     print('file exists %s' % fileRef)
    #     log.userl.info('file exists %s' % fileRef)
    # else:
    #     log.userl.critical('file not found!  %s' % fileRef)
    #     #sys.exit('put ABEND logic here')

#mydict = dict((rows[0],rows[1]) for rows in reader)