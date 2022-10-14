import random, time

list = []
maxNum = 10000
for i in range(maxNum, 0, -1):
    rndNum = random.randint(1,maxNum)
    while rndNum in list:
        rndNum = random.randint(1,maxNum)
    list.append(rndNum)


def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        min_id = i
        for j in range(i+1, len(unsortedList)):
            if unsortedList[min_id] > unsortedList[j]:
                min_id = j
        unsortedList[i], unsortedList[min_id] = unsortedList[min_id],unsortedList[i]
    return unsortedList

def bubbleSort(unsortedList):
    for i in range(len(unsortedList)-1, 0, -1):
        for j in range(i):
            if unsortedList[j] > unsortedList [j+1]:
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
    return unsortedList

def insertionSort(unsortedList):
    for i in range(1, len(unsortedList)):
        key = unsortedList[i]
        j = i-1
        while j >= 0 and key < unsortedList[j]:
            unsortedList[j+1] = unsortedList[j]
            j -= 1
        unsortedList[j+1] = key
    return unsortedList


start = time.time()
insertionSort(list)
print("Insertion sort: ")
print(time.time() - start)

list = []
for i in range(maxNum, 0, -1):
    rndNum = random.randint(1,maxNum)
    while rndNum in list:
        rndNum = random.randint(1,maxNum)
    list.append(rndNum)

start = time.time()
selectionSort(list)
print("Selection sort: ")
print(time.time() - start)

list = []
for i in range(maxNum, 0, -1):
    rndNum = random.randint(1,maxNum)
    while rndNum in list:
        rndNum = random.randint(1,maxNum)
    list.append(rndNum)

start = time.time()
bubbleSort(list)
print("Bubble sort: ")
print(time.time() - start)


