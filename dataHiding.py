class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

person1 = Person("ABC", 22)
print(person1._Person__name)   #you need to add _Class before __Variable to acess the variable
print(person1._Person__age)