import urllib
import urllib.request
import _custom_modular
import _custom_modular as _custom
from _custom_modular import muliply
#does not restrict direct imports of modules or members from a package
from my_package import *

response = urllib.request.urlopen("http://google.com")
html = response.read()
# print(html)

print(_custom_modular.add(2,7))
print(_custom.subtract(2,7))
print(muliply(2,7))
print(dir(_custom))
test_module.third() #will raise ImportError