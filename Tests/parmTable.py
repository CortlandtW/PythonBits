import appStartLogging as log

msg_requiredColumnMissing = 'Required column not found in parameter file.  Column name = "%s"'
requiredColumnNames = ['ID', 'URL', 'URL-Filters', 'Recipient-Email-Address', 'Recipient-Name',
                           'Output-Path', 'Output-File-Name', 'Output-Format', 'Subject-Line',
                           'Body-Line', 'Process']
class parmFileRec():
    """
    Data Structure for main parameter file record.
    """
    missingColumnsCnt = 6       # Count of required columns not found
    id = None
    url = None

    def assertColumn(self, columnName):
        try:
            colValue = self.rowDict[columnName]
            self.missingColumnsCnt -= 1
            return colValue
        except Exception, eArgs:
            log.userl.critical(msg_requiredColumnMissing % columnName)
            return None

    def __init__(self, rowDict):
        self.rowDict = rowDict
        self.id = self.assertColumn('ID')
        self.url = self.assertColumn('URL')
        self.urlFilters = self.assertColumn('URL-Filters')
        self.recipientEmailAddress = self.assertColumn('Recipient-Email-Address')
        self.recipientName = self.assertColumn('Recipient-Name')
        self.subjectLine = self.assertColumn('Subject-Line')

