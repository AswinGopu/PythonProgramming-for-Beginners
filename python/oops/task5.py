class A():
    def __init__(self,x):
        self.x=x
    def display(self):
        i=1
        while i<self.x:
            j=1
            while j<self.x:
                print(i*j,end=" ")
                j+=1
            print()
            print()
            i+=1

class B(A):
    def __init__(self,x):
        A.__init__(self,x)
        self.x=x
    def display1(self):
        for i in range(1,11):
            print(i,"*",self.x,"=",i*self.x)

ob=B(int(input("enter the number")))
ob.display()
ob.display1()
            