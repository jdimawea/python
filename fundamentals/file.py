num1 = 42 # variable declaration, primitive number
num2 = 2.3 # variable declaration, primitive number
boolean = True # Data type, Boolean
string = 'Hello World' #Data type, primitive string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary boolean
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, list strings 
print(type(fruit)) #log statement, tuples
print(pizza_toppings[1]) #log statement, list string
pizza_toppings.append('Mushrooms')  #variable declaration, 
print(person['name']) #log statement
person['name'] = 'George' 
person['eye_color'] = 'blue'
print(fruit[2]) #log statement

if num1 > 45: # if, variable, number
    print("It's greater") #log statement, string
else: # else
    print("It's lower") #log statement, string

if len(string) < 5: #if, function, string
    print("It's a short word!") #log statement, string
elif len(string) > 15: #else if, function
    print("It's a long word!") #log statement, string
else: # else
    print("Just right!") #log statement, string

for x in range(5): #for loop
    print(x) #log statement, variable
for x in range(2,5): #for loop, variable, function
    print(x) #log statement
for x in range(2,10,3): #for loop, variable, function
    print(x) #log statement
x = 0 #function
while(x < 5): #while loop, start, stop
    print(x) #log statement
    x += 1 #variable

pizza_toppings.pop() #variable declaration, function
pizza_toppings.pop(1) #variable declaration, function

print(person) #log statement
person.pop('eye_color') #variable declaration, function, string
print(person) #log statement

for topping in pizza_toppings: #for loop, data type
    if topping == 'Pepperoni': #conditional, string
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional, data type, string
        break #break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #log statement

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)