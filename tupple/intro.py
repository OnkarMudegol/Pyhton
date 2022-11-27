tuple1 = ("apple","grapes")             #intro to tuples
print(tuple1)
tuple2 = ("car", "bike", "boat", "jet")   #printing indexes
# print(tuple2[2])
list1 = list(tuple2)                      #changing tuple to lists
list1.append("cycle")
tuple3 = tuple(list1)
print(tuple3)