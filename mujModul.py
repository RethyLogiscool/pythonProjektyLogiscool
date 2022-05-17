# Můj modul sdružující časté funkce využívané v Pythonu

details = {
    "exampleList" : [9, 8, 7, 6, 5, 4, 3, 2, 1],
}

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