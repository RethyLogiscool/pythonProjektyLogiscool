"""
list = ["Adam","Vojta","Miloš","Antonín","Adam"]
print(list)
print(list[3])
print(list[-1])
print(list[1:3])
print(list[:2])
print(list[2:])

print(len(list))
print(list.__len__())

for jmeno in list:
    print(jmeno)
print("___")

for i in range(list.__len__()):
    print(list[i])
print("___")

i = 0
while i < len(list):
    print(list[i])
    i += 1

list.append("Matěj")

print(list)

numbers = []
for i in range(1,51):
    numbers.append(i)

print(numbers)




sudy = []
licha = []

for i in range(int(input("DO: "))+1):
    if i % 2 == 0:
        sudy.append(i)
    else:
        licha.append(i)

print(sudy)
print(licha)

list_1 = [1,2,3,4,5]
list_2 = [11,23,34,45,56]

for i in range(len(list_1)):
    temp = list_1[i]
    list_1[i] = list_2[i]
    list_2[i] = temp

print(list_1)
print(list_2)

list_1, list_2 = list_2, list_1

print(list_1)
print(list_2)
"""
list = []

list.append(10)
list.append(123)
list.insert(1,115)
list.insert(1,99)
list.insert(100000,10)
list.insert(5000,90)

list[:] = (x for x in list if x != 10)

list.extend([123,1235,542,35424])
print(list)

count = 0
value = 123
for n in list:
    if n == value:
        count += 1

print(f"Číslo {value} se tam vyskytuje {count} krát")


enToCs = {
    "dog" : "pes",
    "cat" : "kočka",
    "apple" : "jablko",
    "door" : "dveře"
    }
enToCs["computer"] = "počítač"
enToCs["game"] = "hra"

enToCs.update({"water":"voda"})

print(enToCs["cat"])
print(enToCs["computer"])

usersPoints = {"david":6,"honza":3}

print(usersPoints["david"])

users = [
    {
        "jméno" : "david",
        "email" : "david@seznam.cz",
        "věk" : 12
    }
]

print(users[0]["jméno"])

