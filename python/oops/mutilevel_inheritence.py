class A():
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class B(A):
    def __init__(self,name,place):
        A.__init__(self,name)
        self.place=place
    def display1(self):
        print(self.place)

class C(B):
    def __init__(self,name,place,age):
        B.__init__(self,name,place)
        self.age=age
    def display2(self):
        print(self.age)

ob=C("aswin","kollam",23)
ob.display()
ob.display1()
ob.display2()

