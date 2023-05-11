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
ob=A(6)
ob.display()



# <second section>


class A():
    
    def display(self):
        x=int(input("enter the number"))

        i=1
        while i<x:
            j=1
            while j<x:
                print(i*j,end=" ")
                j+=1
            print()
            print()
            i+=1
ob=A()
ob.display()