#instance methods - the methods dependent on the object we make
class Students:
    numberOfSubjects = 5   #class var
    def __init__(self, marks1, marks2, marks3):
        self.web = marks1
        self.python = marks2
        self.maths = marks3
    def markAvg(self):
        print("Average marks is:",((self.web+self.python+self.maths)/3))
    # def getMarks(self):
    #     return self.maths    #Accesor - read only or getter
    # def setMarks(self, marks):
    #     self.maths = marks    #Mutators - modify or setter
    @classmethod
    def classMethodExample(cls):
        return Students.numberOfSubjects
    @staticmethod
    def staticMethodExample():
        print("This is  an example of static method")
student1 = Students(5,6,8)
student2 = Students(10,10,10)
student3 = Students(9,8,10)
student1.markAvg()
student2.markAvg()
student3.markAvg()
print(Students.classMethodExample())
print(Students.staticMethodExample)