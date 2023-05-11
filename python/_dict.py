mydict = {"name": "aswin",
          "place": "kollam",
          "subject": "python",
          "age": 23}

print(mydict)
print(mydict.get('place'))
print(mydict.values())
print(mydict.items())
print(mydict.keys())

for kv in mydict.items():
    print(kv)

for vl in mydict.values():
    print(vl)

for k in mydict.keys():
    print(k)

