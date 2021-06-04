from mymodule import my_func #mymodule is file name
from MyMainPackage import mainpackage #MyMainPackage is folder and mainpackage is file
from MyMainPackage.SubPackage import subpackage #SubPackage is child folder of MyMainPackage

mainpackage.main_func()
subpackage.sub_func()
my_func()