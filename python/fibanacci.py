
def prime(n):
    a=0
    b=1
    x=0
    for i in range(0, n):
        print(a)
        x = a+b
        a = b
        b = x

prime(10)