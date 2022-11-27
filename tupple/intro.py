tuple1 = ("apple","grapes")              #intro to tuples
print(tuple1)
tuple2 = ("car", "bike", "boat", "jet")  #printing indexes
print(tuple2[2])
list1 = list(tuple2)                     #changing tuple to lists
list1.append("cycle")
tuple3 = tuple(list1)
print(tuple3)
tuple4 = (1,2,3,[4,5,6],7,8)               #lists inside a tuple
print(tuple4[3][1])                      #ascessing elements inside list
tuple4[3][2]=8                             
print(tuple4)