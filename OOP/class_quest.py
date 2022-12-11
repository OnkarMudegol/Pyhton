#make a person class with name and roll no variable and print out
class Person:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def printOutput(self):
        print("Name of student is "+self.name+" and his/her rollno is "+self.rollno)
p1 = Person("ABC", "65")
p2 =Person("VBF", "78")
p1.printOutput()
p2.printOutput()
print(id(p1))
print(id(p2))