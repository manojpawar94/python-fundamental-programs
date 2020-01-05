#!/usr/bin/python
#tuples are immutable and hashable
def main():
    print("Tuple Examples")
    #declaring the empty tuple
    basketOne = ()
    print(basketOne)

    #declaring the single element tuple
    basketTwo = ('Banana',)
    print(basketTwo)
    #tuple is immutable; but we can always reassign tuple
    basketTwo = ('raja','keshava')
    print(basketTwo)

    #declaring multiple element tuple of same datatype
    basketThree = ('Banana','Mango','Orange','Apple','Grapes')
    print(basketThree)

    #declaring multiple element tuple of different datatype
    basketFour = ('Banana', 4, 'Mango', 9.3)
    print(basketFour)

    #Accessing specific element of tuple 
    print("Index 1 element of basketFour's tuple: ", basketFour[1])

    #Accessing slice of element of tuple
    print("Index 1 to 3 element of basketThree's tuple: ", basketThree[1:3])

    #Functions available for tuples
    #reading length of the tuple
    print("The length of tuple basketThree: ", len(basketThree))

    #contacting two or more tuples
    newTuple = basketTwo + basketThree
    print("New Tuple by concatination", newTuple)

    #comparing two tuples
    print(cmp(basketThree,basketFour))

if __name__ == "__main__":
    main()