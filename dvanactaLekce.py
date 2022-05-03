leng = 10
numbers = []
while leng > 0:
    #numbers.append(int(input("Zadej číslo: ")))
    leng -= 1
print(numbers)
odd = 0
even = 0
positive = 0
negative = 0
zero = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

list = [1,2,3,4]
print(list)
list.extend([5,6,7])
print(list)
list.append("1,2")
print(list)

list = [2,3,1.5, "Hello", -2]
intList = []
for i in list:
    if type(i) == int:
        intList.append(i)
print(list)
print(intList)

list = [100, 2, 3, 8, 9, 12, 5, 7, 4, 12]
print("Nejvyšší: " + str(max(list)) + ", 2. nejvyšší: " + str(max(list[:list.index(max(list))]+list[list.index(max(list))+1:])))

maxNum = 0
druMax = 0
treMax = 0
minNum = max(list)
druMin = max(list)
treMin = max(list)
for num in list:
    if num > maxNum:
        maxNum = num
print(maxNum)
for num in list:
    if num > druMax and num != maxNum:
        druMax = num
print(druMax)
for num in list:
    if num > treMax and num != maxNum and num != druMax:
        treMax = num
print(treMax)
for num in list:
    if num < minNum:
        minNum = num
print(minNum)
for num in list:
    if num < druMin and num != minNum:
        druMin = num
print(druMin)
for num in list:
    if num < treMin and num != minNum and num != druMin:
        treMin = num
print(treMin)

