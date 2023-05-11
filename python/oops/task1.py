class Student():
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3 
    def display1(self):
        print(self.name)
    def display2(self):
        print(self.mark1+self.mark2+self.mark3)

ob=Student("aswin",20,20,20)
ob.display1()
ob.display2()

        