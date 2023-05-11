



def prime(a):
    flag=0
    i=2
    while(i<a):
        if a%i==0:        
            flag=1
            break
        i=i+1
    if flag==1:
        print("not a prime")
    else:
        print("prime")  
prime(int(input("enter the number")))
            


            
