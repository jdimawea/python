from flask_app.config.mysqlconnection import connectToMySQL


class Dog: 
    def __init__(self, data):
        #data is a dictionary that holds the data from the DB
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.hair_color = data['hair_color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # CREATE
    @classmethod
    def create(cls, data):
        # Data holds the individula dog data to add a dog to the DB
        # data is a dictionary
        # %(key_in_dict)s
        query = "INSERT INTO dogs (name, age, hair_color, created_at, updated_at) VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());"
        result = connectToMySQL("dogs_erd").query_db(query, data)

        return result


    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        # results contains a list of dictionaries
        # each dictionary is a row in the table
        results = connectToMySQL("dogs_erd").query_db(query)

        # create an empty list to append all instances  of dogs
        dogs = []

        # iterate over the DB results and create dogs
        for row in results:
            # cls(row) == Dog(row) => User() Pizza() => creating an object / instance of the class
            dogs.append(cls(row))

        return dogs


    # UPDATE



    # DELETE