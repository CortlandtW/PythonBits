import ConfigParser
import sys
#import ast
"""
Demonstrate Use of ConfigParser to parse & extract  parameters stored in configuration files.

DEFINITIONS:
The configuration file parsed by ConfigParser can contain sections/section headers, options, and comments.
For example:
    # comment line
    [section1]
    option1=qwertystring
    option2=222
    [section2]
    ...

Vars - a dictionary of values;
    when vars is specified in a .get() method the value found in
    the dictionary overrides anything specified in the config file.
    (In other words it is #1 in the search path.)

SYNTAX:
* Case Insensitive: Section and Option names are not case sensitive.
* The following variations are equivalent:
    option1=qwertyString,  Option1 = queryString
    opt1=1, opt1 = 1, opt1:1, opt1 : 1
* At least 1 section header is required.
    See exception ConfigParser.MissingSectionHeaderError

"""

def printVarStr(sectionName, VarName):      # common function for this demo
    print('Section: %s  Var: %s  = %s' %
          (sectionName, VarName, config.get(sectionName, VarName) ) )

nosuchfileFR1 = "nosuchfile"                # test files
exampleFR1 = 'ConfigParser_example1.txt'

config = ConfigParser.SafeConfigParser()

#------- .read  file does not exist  -----------
print('------ read file that does not exist test -------')
try:
    openedFilesList = config.read(nosuchfileFR1)
except ConfigParser.Error, err:    # no known triggers for bad file reference
    print str(err)
    sys.exit('Cannot continue with this error')

#if openedFilesList == []:
if not nosuchfileFR1 in openedFilesList:
   print('Config file failed to open: %s' % nosuchfileFR1)
# If the config file is not opened then there is nothing
# to parse.  Therefor methods such as
# config.has_section() will ALWAYS return False.

#----------------------------------------------------------
print('\n------ read existing config file ---------')
try:
    openedFilesList = config.read(exampleFR1)

except ConfigParser.MissingSectionHeaderError, err:
    print str(err)
    sys.exit('Cannot continue with this error')
except ConfigParser.ParsingError, err:
    print str(err)
    sys.exit('Cannot continue with this error')
except ConfigParser.Error, err:
    print('ConfigParser.Error - base error class')
    print str(err)
    sys.exit('Cannot continue with this error')

if exampleFR1 in openedFilesList:
    print('Opened config file %s' % exampleFR1)
else:
    sys.exit('some ABEND process here')
#-------- get var, normal case -------
printVarStr('section1', 'var1')

#-------- validating sections are present --------
print('\n------ validate section headers from list  ---------')
for candidateSection in ['section1', 'section2', 'none']:
    print '%-12s: %s' % (candidateSection, config.has_section(candidateSection))
# -------- validating options are present --------
print('\n------ validate options in section from  list  ---------')
# Options are the variables within Sections.
candidateSection = 'section1'
for candidateOption in ['var1', 'var2', 'list1', 'none']:
    if config.has_option(candidateSection, candidateOption):
        printVarStr(candidateSection, candidateOption)
    else:
        print '%-12s: %s' % (candidateSection, config.has_option(candidateSection, candidateOption))

#-------- get string
print('\n------ compare var1 to var2 (strings with different syntax)  ---------')
#  .get() returns a string.  See also .getint(), getfloat(), getboolean()
var1 = config.get('section1', 'var1')
var2 = config.get('section1', 'var2')
if not var1 == var2:
    print('Var1 <> Var2')



#print config.get('xsection1', 'var1')