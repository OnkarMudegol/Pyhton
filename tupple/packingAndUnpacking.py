# tuple1 = (1,2,3,4,5)                     #packing and unpacking tuples
# (one, two, three, four, five) = tuple7
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)
# tuple2 = (one, two, three)
# print(tuple8)

#write a program to unpack following tuple into 4 variable
#tuple3 = (10,20,30,40)
tuple3 = (10,20,30,40)
# for i in tuple3:
#     print(i)
ind = 0
l = len(tuple3)
while l != 0 :
    print(tuple3[ind])
    ind += 1
    l -= 1