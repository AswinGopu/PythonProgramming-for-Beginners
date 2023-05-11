

def prime(a):
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag=1
            break
    if flag==1:
        print("not a prime")
    else:
        print("prime") 
prime(50)   