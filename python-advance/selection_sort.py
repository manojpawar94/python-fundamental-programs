#!/usr/bin/env python
#selection sorting example
numList = [65, 25, 12, 22, 11]
for index in range(len(numList)):
    tempIndex = index
    for iterator in range(index+1,len(numList)):
        if(numList[tempIndex] > numList[iterator]):
            tempIndex = iterator
    numList[index], numList[tempIndex] = numList[tempIndex], numList[index]
print(numList)