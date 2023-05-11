y=0
n=int(input("enter the number"))
a=n
while(n>0):
    x=n%10
    y=y*10+x
    n=n//10
print(y)
print(n)
if y==a:
    print("palintrom")
else:
    print("not a plaintrom")

      
