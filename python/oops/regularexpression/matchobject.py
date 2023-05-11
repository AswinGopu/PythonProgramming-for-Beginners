import re
from tokenize import group


txt = "watson jhony yes pappa"

x = re.search("jhony",txt)
print("object : ",x)
print("span : ",x.span())
print("string : ",x.string)
print("group : ",x.group())