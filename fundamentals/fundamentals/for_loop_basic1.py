# Basic
for x in range(151):
    print(x)

# Multiples of Five
for x in range(5,1001, 5):
    print(x)

#Counting, the Dojo Way
for x in range(1,101,1):
    if x % 5 != 0:
        print(x)
    if x % 10 == 0:
        print ("Coding Dojo")
    elif x % 5 == 0:
        print ("Coding")

#Whoa. That Sucker's Huge
oddSum = 0
for x in range(1,500001,2):
    oddSum = oddSum + x
print(oddSum)

#Countdown by Fours
start = 2018
end = 0
for x in range(start, end, -4):
    print(x)

#Flexible Counter
def countdown(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)

countdown(2,9,3)