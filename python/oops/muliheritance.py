class A():
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class B():
    def __init__(self,place):
        self.place=place
    def display1(self):
        print(self.place)

class C(A,B):
    def __init__(self,age,name,place):
        A.__init__(self,name)
        B.__init__(self,place)
        self.age=age
    def display2(self):
        print(self.age)  

ob=C(23,"aswin","kollam")
ob.display()
ob.display1()
ob.display2()                  