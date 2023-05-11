class Student():
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def display(self):
        print(self.name,self.subject)

ob=Student("aswin","python")
ob.display()