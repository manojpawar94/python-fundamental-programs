#!/usr/bin/env python
#Bubble sorting example
#the wrost case time complexity is order of n^n [O(n^n)], when elements are reversly sorted
#the best case time complexity is order of n [O(n)], when element are correctly sorted
#Auxillary complexity is order of 1 [O(1)]
def bubbleSortAcending(array):
    #iterating over the all elements of array
    for index in range(len(array) - 1):

        for iterator in range(len(array) - 1):
            if array[iterator] > array[iterator + 1]:
                array[iterator], array[iterator+1] = array[iterator + 1], array[iterator]

#optimized implement of bubble sort
def optBubbleSortDescending(array):
    for index in range(len(array) - 1):
        isSwapped = False
        for iterator in range(len(array)-1):
            if array[iterator] < array[iterator + 1]:
                array[iterator], array[iterator + 1] = array[iterator + 1], array[iterator]
                isSwapped = True
        if isSwapped == False:
            break

def main():
    print("Normal Bubble Sort:")
    numList = [65, 25, 12, 22, 11, 45]
    
    print("Before Sorting:")
    print(numList)
    bubbleSortAcending(numList)
    print("After Sorting using bubble sort")
    print(numList)

    print("\nOptimized Bubble Sort:")
    print("Before Sorting:")
    print(numList)
    optBubbleSortDescending(numList)
    print("After Sorting using optimized bubble sort")
    print(numList)

    print("\nRecursive Bubble Sort:")
    print("Before Sorting:")
    print(numList)
    recursiveBubbleSort(numList, len(numList))
    print("After Sorting using recursive bubble sort:")
    print(numList)

def recursiveBubbleSort(numList, length):
    if length == 1: return
    for index in range(len(numList)-1):
        if numList[index] > numList[index + 1]:
            numList[index], numList[index + 1] = numList[index + 1], numList[index]
    recursiveBubbleSort(numList, length - 1)

if __name__ == '__main__':
    main()