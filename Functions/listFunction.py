#create a function to separate even numbers from a list
list1 = [3,2,8,16,11,34,17]
output=list(filter(lambda i:i%2==0,list1))
print(output)
output2=list(filter(lambda i: i>15,list1))
print(output2)
output3 = list(map(lambda i:i**2,list1))
print(output3)