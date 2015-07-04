import globalConfig
import globalMod2



def set_x(val):
    globalConfig.xglobal = val

def print_x():
    print('Print from %s ; value of x = %s' % (__name__, globalConfig.xglobal))
