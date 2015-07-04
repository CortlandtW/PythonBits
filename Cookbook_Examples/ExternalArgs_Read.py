import argparse
import sys
"""
.ArgumentParser Options:
    usage = - not recommended.  Overwrites default usage text which is pretty good.
.add_argument Options:
    action = 'store'.  Default.
        Stores the value given after the tag.
    action = 'store_true'
            ('--foo', action='store_true') saves True when '--foo'
            is given as argument.
    type=argparse.FileType - only helpful when a complete file reference is passed.
    action = 'version' - Requires a version= argument.
       Prints information specified by the version= argument and exits when invoked.
       Example:  parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    nargs = n : n arguments allowed; stored in a list
    nargs = '*': any number of arguments; stored in a list
    nargs = '+': 1 argument required, more allowed; stored in a list
    nargs = ? : 1 argument allowed; if not present use value from default=
"""
# usage = 'Usage example: ______',aa
parser = argparse.ArgumentParser(
    description='demonstrate use of argparse for processing command line arguments/parameters',
    epilog='Final words.')
parser.add_argument( "-requiredStr", dest='req', required=True,
                    type=str,
                    help="file reference to parameters.csv file ")
parser.add_argument("-commonparms",   type=str,
                    help="file reference to common parameter file ")
parser.add_argument("-csv", dest='csv',
                    type=argparse.FileType(mode='r'),
                    help="file reference to parameters.csv file ")


args = parser.parse_args()      # default source of text to parse is sys.argv
                                # Arguments can be entered here - helpful for experimentation
                                # args is an object of class argparse.Namespace
                                # var(args) converts args to a dictionary.


try:
    #csvFileRef = args.csv  # args is a dictionary containing the arguments
    #staticParmRef = args.commonparms
    #print(args.requiredStr)
    print(args.req)
    #print(staticParmRef)
    #print(csvFileRef)
except argparse.ArgumentError, err:          # don't know what this is, no traps from this
    print(' .ArgumentError: %s ' % err)
except AttributeError, err:                 # Undocumented -- it works!
    print(' except AttributeError: %s ' % err)
except Exception, err:                      # slighly more generic message
    print(' General Exception: %s ' % err)

print('All arguments: %s' % vars(args))


# ===============================
# Example - custom validation
# def is_valid_file(parser, arg):
#     if not os.path.exists(arg):
#         parser.error("The file %s does not exist!" % arg)
#     else:
#         return open(arg, 'r')  # return an open file handle
#
#
# parser = ArgumentParser(description="ikjMatrix multiplication")
# parser.add_argument("-i", dest="filename", required=True,
#                     help="input file with two matrices", metavar="FILE",
#                     type=lambda x: is_valid_file(parser, x))
# args = parser.parse_args()
#
# ------------------------------
# Example 2:
# def extant_file(x):
#     """
#     'Type' for argparse - checks that file exists but does not open.
#     """
#     if not os.path.exists(x):
#         raise argparse.ArgumentError("{0} does not exist".format(x))
#     return x
#
# if __name__ == "__main__":
#     import argparse, sys, os
#     from argparse import ArgumentParser
#
#     parser = ArgumentParser(description="ikjMatrix multiplication")
#     parser.add_argument("-i", "--input",
#         dest="filename", required=True, type=extant_file,
#         help="input file with two matrices", metavar="FILE")
#     args = parser.parse_args()
