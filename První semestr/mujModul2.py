
_exampleList = [9, 5, 1, 4]

def changeExampleList(inputList):
    global _exampleList
    _exampleList = inputList

def getExampleList():
    return _exampleList


def selectionSort(unsortedList=None):
    if(not unsortedList):
        unsortedList = _exampleList
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