myset1 = {"AMG-GT R","m3","911","GTR","Impereza"}
myset2 = {"Civic","Polo","Impereza"}
myset1.add("AstonMartin")
print(myset1)
(myset1.update({"AlfaRome","Mclaren"}))
print(myset1)
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.symmetric_difference(myset2))