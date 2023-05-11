from os import mkdir


import os
# mkdir("asd")
# open("asd\helo.txt","x")
a=open("asd\helo.txt","w")
a.write("welcome world.....!")
a.close()
a=open("asd\helo.txt","r")
print(a.read())

