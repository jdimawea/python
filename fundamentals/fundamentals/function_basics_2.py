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
