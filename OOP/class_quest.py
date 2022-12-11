#make a person class with name and roll no variable and print out
class Person:
    def __init__(self, name, rollno, age):
        self.name = name
        self.rollno = rollno
        self.age = age
    def printOutput(self):
        print("Name of student is "+self.name+" and his/her rollno is "+self.rollno)
    def changeName(self):
        self.name = "Amcf"
    def sameAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False
            
p1 = Person("ABC", "65", "16")
p2 =Person("VBF", "78", '16')
p1.printOutput()
p2.printOutput()
# print(id(p1))
# print(id(p2))
# p1.name = "xyz" #changing the assigned name of p1
print(p1.name)
p1.changeName()
print(p1.name)
if p1.sameAge(p2):
    print("They are of same age")
else:
    print("They are of different age")
p1.age = 18
if p1.sameAge(p2):
    print("They are of same age")
else:
    print("They are of different age")