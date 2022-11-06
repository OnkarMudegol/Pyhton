#to print keywords with data set
def info(name, **data):
    print(name)
    print(data)
info("XYZ", age=34, place="dehradun")
#it becomes a dictionary as keywords are defined
def info(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
info("Onkar", age=18, place="Aurangabad")