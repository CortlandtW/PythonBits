import globalMod1
import globalConfig
import globalConfig as config2

print('x from config2 init = %s' % config2.xglobal)
print('x init = %s' % globalConfig.xglobal)


globalMod1.print_x()

globalMod1.set_x('set by set_x called from main')
globalMod1.print_x()
print('x (set to 22) = %s' % globalConfig.xglobal)