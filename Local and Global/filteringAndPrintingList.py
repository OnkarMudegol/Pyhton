# create a function that will display how 
# many items in the list have more than five characters
#names = ["Tom","Jerry","Sunio","Doraemon","Mii-Chan","Nobita","Shizuka","Gian"]
count = 0
def name_count(names):
    global count
    for i in names:
        l = len(i)
        if len(i)>5:
            count = count+1
            print(i)
    print(count)
names = ["Tom","Jerry","Sunio","Doraemon","Mii-Chan","Nobita","Shizuka","Gian"]
name_count(names)
