#Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def changeValue():
    x[1][0] = 15
    students[0]['last_name'] = 'Bryant'
    sports_directory['soccer'][0] = 'Andres'
changeValue()
print(x)
print(students)
print(sports_directory)

#Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        for key, val in some_list[i].items():
            print("{} - {}".format(key, val))

iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for val in some_list:
        print(val[key_name])

iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    print(len(some_dict['locations']),"Locations")
    for l in some_dict['locations']:
        print(l)
    print(len(some_dict['instructors']),"Instructors")
    for i in some_dict['instructors']:
        print(i)

printInfo(dojo)

