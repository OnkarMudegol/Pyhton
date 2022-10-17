#to learn anout nested if and else
a = 200 
if a < 500:
    print("A is less than 500")
    if (a < 300):
        print("A is less than 300")
    elif a== 200:
        print("A is 200")
    else:
        print("Nothing")
elif a < 200:
    print("A is less than 200")
else:
    print("Else will print")
print("Hello World")