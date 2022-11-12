#copying list and pasting in another
num1 = [1,5,67,88,96,23]
num2 = num1.copy()
print(num2)
indx = num1.index(5)
num1[indx]=100
print(num1)