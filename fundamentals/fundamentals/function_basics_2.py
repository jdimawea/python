#countdown
myRange=[]
def countDown(x):
    for x in range(x,0 - 1, -1):
        myRange.append(x)
    return myRange
print(countDown(5))

#print and return
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

#first plus length
def first_plus_length(list):
    x = len(list)
    return(list[0] + x)
print(first_plus_length([3,4,5,6,7]))

#values greater than second
newList = []
def values_greater_than_second(list):
    for val in list:
        if val > list[1]:
            newList.append(val)
    if len(list)<2:
        return False
    print(len(newList))
    return newList
print(values_greater_than_second([2,3,4,5,6,7,1]))
print(values_greater_than_second([]))

# This Length, That Value
def length_and_value(x,y):
    myList = []
    for i in range(x):
        myList.append(y)
    return myList
print(length_and_value(10,3))
