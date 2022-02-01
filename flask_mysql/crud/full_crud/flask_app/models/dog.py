from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import collar

# Model file, Model class
class Dog:
    def __init__(self, data):
        # data is a dictionary that holds the data from the DB
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.hair_color = data['hair_color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.collars = []


    # CREATE
    @classmethod
    def create(cls, data):
        # Data holds the individual dog data to add a dog to the DB
        # data is a dictionary
        # %(key_in_dict)s
        query = "INSERT INTO dogs (name, age, hair_color, created_at, updated_at) VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());"

        # docstring """
        query = """
            INSERT INTO dogs (name, age, hair_color, created_at, updated_at) 
            VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());
        """

        # 
        query = "INSERT INTO dogs (name, age, hair_color, created_at, updated_at)" \
            "VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());"

        query = (
            "INSERT INTO dogs (name, age, hair_color, created_at, updated_at)"
            "VALUES (%(name)s, %(age)s, %(hair_color)s, NOW(), NOW());"
        )

        result = connectToMySQL("dogs_erd").query_db(query, data)

        return result


    # READ
    # Read Many
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        # results contains a list of dictionaries
        # each dictionary is a row in the table
        results = connectToMySQL("dogs_erd").query_db(query)

        # create an empty list to append all instances of dogs
        dogs = []

        # iterate over the DB results and create dogs
        for row in results:
            # cls(row) == Dog(row) => User() Pizza() BankAccount() => creating an object / instance of the class
            dogs.append(cls(row))
            
        return dogs


    # Read One
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"

        # results is still a list of dictionaries
        results = connectToMySQL("dogs_erd").query_db(query, data)

        return cls(results[0])
    

    @classmethod
    def get_dog_with_collars(cls, data):
        query = "SELECT * FROM dogs LEFT JOIN collars ON dogs.id = collars.dog_id WHERE dogs.id = %(id)s;"

        results = connectToMySQL("dogs_erd").query_db(query, data)

        this_dog = cls(results[0])

        print(results)
        if results[0]["collars.id"] != None:
            for row_data in results:
                collar_data = {
                    "id": row_data["collars.id"],
                    "color": row_data["color"],
                    "dog_id": row_data["dog_id"],
                    "created_at": row_data["collars.created_at"],
                    "updated_at": row_data["collars.updated_at"]
                }
                this_dog.collars.append(collar.Collar(collar_data))

        return this_dog


    # UPDATE
    @classmethod
    def update(cls, data):
        # data is a dictionary that holds the information we want to update the DB with
        print(data)
        query = "UPDATE dogs SET name = %(name)s, age = %(age)s, hair_color = %(hair_color)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL("dogs_erd").query_db(query, data)


    # DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"

        connectToMySQL("dogs_erd").query_db(query, data)