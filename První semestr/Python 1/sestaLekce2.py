names = ["Anna","Bára","Honza","David"]
print(names)
print(type(names))

print(len(names))
print(names[len(names)-1])
print(names[-1])
print(names[0])
print(names[1:3])
print(names[-2:])

for name in names:
    print(name)

for i in range(len(names)):
    print(names[i])

i = 0
while i < len(names):
    print(names[i])
    i += 1

numbers = []
i = 0
while i < 51:
    numbers.append(i)
    i += 1
print(numbers)

numbers = []
for i in range(1,51):
    numbers.append(i)
print(numbers)
print("____")

list_1 = [1,2,3,4,5]
list_2 = [11,12,23,34,45]
print(list_1)
print(list_2)

for i in range(len(list_1)):
    temp = list_1[i]
    list_1[i] = list_2[i]
    list_2[i] = temp
print(list_1)
print(list_2)

print("____")

list = []

list.insert(10,1)
list.insert(0,2)
print(list)
list.append(300)
list.append(5)
list.append(5)
list.append(1)
print(list)
list.insert(0,5)
print(list)
list.pop(1)
print(list)
list.remove(300)
print(list)

count = 0
value = 5
for n in list:
    if n == value:
        count += 1
print("Číslo {0} se v listu objevuje {1} krát.".format(value,count))

enToCs = {"apple":"jablko","orange":"pomeranč"}
print(enToCs["apple"])

dict = {}
for n in list:
    if n in dict.keys():
        count = dict[n]
        count+=1
        dict[n] = count
    else:
        dict[n] = 1

print(dict)