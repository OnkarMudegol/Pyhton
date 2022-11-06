# Create a function for the following condition
# It should accept employee name and salary and display both
# If the salary is missing in the finction then assign the defaut value 10000 to salary
def statement(name,salary=10000):
    print(name,salary)
statement("Ramesh",250000)
statement("Suresh")