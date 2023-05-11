class Student():
    def __init__(self,name,name1,name2,mark1,mark2,mark3):
        self.name=name
        self.name1=name1
        self.name2=name2
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def display1(self):
        print(self.name)
    def display4(self):
        print(self.mark1+self.mark2+self.mark3)
    def display2(self):
        print(self.name1)
    def display5(self):
        print(self.mark1+self.mark2+self.mark3)
    def display3(self):
        print(self.name2)    
    def display6(self):
        print(self.mark1+self.mark2+self.mark3)        
ob=Student("aswin","arun","kiran",20,20,20)
ob.display1()
ob.display4()
ob.display2()
ob.display5()
ob.display3()
ob.display6()

class student():
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print(self.name,self.mark)

ob=student("aswin",25)
ob.display()
ob=student("Durga",30)
ob.display()
