# to get fibonacci Series 
def getFibonacciSeries(endNumber = 10):
    result = []
    numberOne, numberTwo = 0, 1
    while numberOne < endNumber:
        result.append(numberOne)
        numberOne, numberTwo = numberTwo, numberOne + numberTwo
    return result

# to check whether number is even
def isEven(number):
    if(number % 2 == 0):
        return True
    else:
        return False
        
# to check whether number is prime
def isPrime(number):
    for index in range(2, number):
        if number % index == 0 :
            return False
    else :
        return True


#print(getFibonacciSeries())
print(isPrime(4))