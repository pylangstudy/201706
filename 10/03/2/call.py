#from package1.package11 import * 
#from package1 import * 
#from package1.package11.module1 import *
from package1.package11 import module2
print(dir())

#import package.module2
module2.some_method()
#package11.module2.some_method()
#package1.package11.module2.some_method()

#import package.module1
