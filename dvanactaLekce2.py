numbers = []
for i in range(10):
    #numbers.append(int(input("Přidej číslo do listu: ")))
    print("")
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
list.extend("Ahoj")
print(list)

list = [2,3,1.5,"Hello",-2]
intList = []
for i in list:
    if type(i) == int:
        intList.append(i)
print(list)
print(intList)

list = [-100, -1, -5, -2, -3, -8, -12, -7, -4]
print("Nejvyšší: " + str(max(list)) + ", 2. nejvyšší: " + str(max(list[:list.index(max(list))]+list[list.index(max(list))+1:])))

maxNum = float('-inf')
druMax = float('-inf')
for num in list:
    if num > maxNum:
        maxNum = num
print(maxNum)
for num in list:
    if num > druMax and num != maxNum:
        druMax = num
print(druMax)