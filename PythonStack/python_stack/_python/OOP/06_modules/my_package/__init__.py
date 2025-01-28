#Reqired in python 2.7 
#Needed to indicate that the files in the folder were part of the package

#Python 3.3+ need to customize the modules available 
#to anyone attempting to import the package

##to avoid other other_module or third_module to be access
# for importing 
#override the __all__ variable

from my_package import *
__all__ = ["test_module"]
