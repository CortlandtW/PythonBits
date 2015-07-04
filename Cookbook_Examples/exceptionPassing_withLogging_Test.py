import SMPTMailer
import sys
import logging

#logging.basicConfig(filename='example.log',level=logging.DEBUG)
# debug, info, warning, error, critical
logging.basicConfig(level=logging.DEBUG)
logx = logging.getLogger()
logx.info('xx Info level log')

#sys.exit('stop here')

print 'Exception Passing Test'
mserv = SMPTMailer.DeliverEmail()
if not mserv.connect():
   sys.exit('connect Failed!')
try:
    mserv.format()
except Exception, eArgs:
    logx.info('has exception = "Exception"')
    logx.exception('info from logger:')
    #l.critical('critical == ',exc_info=True)
    sys.exit('exit - error in format!')

#print 'message formatted'
#if not mserv.sendmail():
#   sys.exit('sending of email message failed!')   
#print 'email message sent' 