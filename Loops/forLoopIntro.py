#Intro to for loop
cars = ["Defender", "GTR", "G-Wagon", "Koenisegg"]
for i in cars:
    if i == "G-Wagon":
        continue
    print(i)
print()
bikes = ["BMW", "Royal Enfield", "Bajaj", "Honda"]
for i in bikes:
    if i == "Bajaj":
        break
    print(i)

for i in range(2,11,2):
    print(i)

