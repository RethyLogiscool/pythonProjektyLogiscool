names = ["Anna","Bára","Daniela","Lucka","Jan","Ondra","Lukáš","Martin"]
print(names)
print(type(names))
print("")

print(len(names))
print(names[0])
print(names[1])
print(names[1:4])
print(names[-3])

for name in names:
    print(name)
print("____")
for i in range(len(names)):
    print(names[i])
print("____")
i = 0
while i < len(names):
    print(names[i])
    i += 1
print("____")
print(", ".join(names))

numbers = []
i = 1
while i <= 50:
    numbers.append(i)
    i += 1
print(numbers)

"""
vstup bude: číslo kterým řada skončí (N)

dva listy (studá a lichá čísla)
vygenerovat řadu čísel od 0 do N
čísla přiřadit ke dvěma listům podle toho jestli jsou sudá nebo lichá

výstup bude: dva listy sudých a lichých čísel

"""
"""
od = int(input("Vyber začatek listu: "))
do = int(input("Vyber konec listu: "))
suda = []
licha = []

for i in range(od, do+1):
    if i%2 == 0:
        suda.append(i)
    else:
        licha.append(i)
print(suda)
print(licha)
"""

list_1 = [1,2,3,4,5]
list_2 = [11,23,34,45,56]
print(list_1)
print(list_2)

for i in range(len(list_1)):
    temp = list_1[i]
    list_1[i] = list_2[i]
    list_2[i] = temp

print(list_1)
print(list_2)
print("")

list = []

list.insert(0,1)
list.insert(1,5)
list.insert(2,15)
list.insert(1,3)
#[1, 3, 4, 5, 15]
list.insert(2,4)
list.insert(1,2)
list.insert(300,5)
list.append(15)
list.append(1)
list.append(8)
list.append(22)
list.append(5)
list.append(1)
print(list)

girl_names = ["Anna","Marie","Lucie"]
boy_names = ["Tomáš","Martin","Honza","Tomáš"]
print(girl_names)
print(boy_names)
girl_names.pop(2)
boy_names.remove("Tomáš")
print(girl_names)
print(boy_names)

"""
count = 0
value = int(input("Jaké číslo hledáš?"))
for n in list:
    if n == value:
        count += 1
print("Číslo {0} se tam vyskytuje {1}".format(value,count))
"""



dict = {}
for n in list:
    if n in dict.keys():
        count = dict[n]
        count+=1
        dict[n] = count
    else:
        dict[n] = 1

print(dict)

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

