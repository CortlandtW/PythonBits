# as of Dec 2013
#SMTP: smtp.gmail.com
#User: dsbi@dataself.com
#Pw: SanJose408
#Use Authentication: Yes
#Ports: 587 (or 465)
#from RunTimeParms import RunParms     # 'global'/(app level) run time parameters
import logging
import unittest
from email.MIMEText import MIMEText
# Import smtplib for the actual sending function
import smtplib
import sys

MailServerName = 'smtp.gmail.com:587'
MailServerName = 'smtp.gmail.com'
MailUser = 'dsbi@dataself.com'
MailPw = 'SanJose408'
ToAddrs = 'cwilson@dataself.com'


class DeliverEmail(object):
    def connect(self):
        logx.info(' Attempting to Connect to SMPT (email) server. ')
        self.abend = True
        try:
            s = smtplib.SMTP(MailServerName, 587)
        except smtplib.SMTPException, eArgs:
            logx.error('SMTPException during connect attempt')
            logx.critical(eArgs.message)
            self.abend = True
            return False
        except Exception, eArgs:
            logx.critical(
                'General exception during SMTP server connect attempt -may be due to bad smtp server address or port #')
            logx.critical(eArgs)
            return False
        try:
            s.set_debuglevel(0)

            s.ehlo()  # identify ourselves, prompting server for supported features
            if s.has_extn('STARTTLS'):  # If we can encrypt this session, do it
                s.starttls()
                s.ehlo()  # re-identify ourselves over TLS connection

            s.login(MailUser, MailPw)
        except smtplib.SMTPConnectError, sceArgs:  # expected but not raised when bad host or port
            logx.error('SMTPConnectError. Error occurred during establishment of a connection with the server.')
            logx.error(ceArgs)
            self.abend = True
            return False
        except smtplib.SMTPAuthenticationError, aeArgs:
            logx.critical(
                'SMTP Authentication Error. Probably the server didn\'tfix accept the '                  'username/password combination provided.')
            logx.critical(aeArgs)
            self.abend = True
            return False
        except smtplib.SMTPException, eArgs:
            logx.critical(eArgs.message)
            self.abend = True
            return False
        except Exception, eArgs:
            logx.critical('General exception during SMTP server login')
            logx.critical(eArgs)
            self.abend = True
            return False
        logx.info('Connectioned and logged in to SMTP server. ')
        self.s = s
        self.abend = False
        return True

    def format(self):
        # plain text message
        self.msg = MIMEText('Hello world!\r\n', 'plain')
        self.msg['Subject'] = 'Subject of message'
        self.msg['From'] = MailUser
        self.msg['To'] = ToAddrs

    def sendmail(self):
        self.abend = True
        try:
            self.s.sendmail(MailUser, ToAddrs, self.msg.as_string())
        except smtplib.SMTPException, eArgs:
            logx.error('SMTPException during attempt to send email.')
            logx.error(eArgs.message)
            return False
        self.s.quit()

        self.abend = False
        return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logx = logging.getLogger()
    logx.info("__name__ == '__main__'")
    mserv = DeliverEmail()
    if not mserv.connect():
        sys.exit('connect Failed!')
    mserv.format()
    print 'message formatted'
    if not mserv.sendmail():
        sys.exit('sending of email message failed!')   
 
    
