# open("as.txt","x")
a=open("as.txt","w")
a.write("wlcome world")

pos=a.tell()
print("current position :",pos)
print(a.seek(0,2))
# print("rest current position :",pos)
