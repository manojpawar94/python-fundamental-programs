def getCubeSeries(startNumber =1, endNumber = 10 ):
    result = []
    for index in range(startNumber,endNumber + 1):
        result.append(index ** 3)
    return result

cubeSeries = getCubeSeries(startNumber = 5)
print("Original Series:", cubeSeries, "The number of elments:", len(cubeSeries))
cubeSeries.insert(0,0)
print("After Insert function:", cubeSeries, "The number of elments:", len(cubeSeries))
cubeSeries.remove(0)
print("After Remove function:", cubeSeries, "The number of elments:", len(cubeSeries))

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("The number of bananas in fruits:", fruits.count("banana"))
print("The index of apple", fruits.index('apple'))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
element = fruits.pop()
print(element)
print(fruits)
element = fruits.pop(2)
print(element)
print(fruits)