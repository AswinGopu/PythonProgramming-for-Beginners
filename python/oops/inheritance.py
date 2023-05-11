class A():
    def __init__(self,name):
        self.name=name
    def display(self):
        print (self.name)

class B(A):
    def __init__(self,mark,name):
        A.__init__(self,name)
        self.mark=mark
    def display1(self):
        print(self.mark)

ob=B(50,"aswin")
ob.display()
ob.display1()                    