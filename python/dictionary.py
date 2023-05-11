dict1 = {"name": "aswin",
         "place": "kollam",
         "subject": "python",
         "age": 23}

print(dict1["name"])
print(dict1["age"])
for i in dict1:
    print(i)
    print(dict1[i])

dict1["age"]=25
dict1["contact"]=2023256548


dict1.pop("contact")
dict1.popitem()
del dict1["subject"]
dict1.clear()
del dict1
print(dict1)
