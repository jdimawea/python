from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dog


class Collar:
    def __init__(self, data):
        self.id = data['id']
        self.dog_id = data['dog_id']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dog = dog.Dog.get_one({"id": data["dog_id"]})

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO collars (dog_id, color, created_at, updated_at) VALUES (%(dog_id)s, %(color)s, NOW(), NOW());"

        # what does the INSERT query return?
        # it returns the id of the newly created row
        return connectToMySQL("dogs_erd").query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM collars;"
        # results contains a list of dictionaries
        # each dictionary is a row in the table
        results = connectToMySQL("dogs_erd").query_db(query)

        # create an empty list to append all instances of collars
        collars = []

        # iterate over the DB results and create collars
        for row in results:
            # cls(row) == Dog(row) => User() Pizza() BankAccount() => creating an object / instance of the class
            collars.append(cls(row))
            
        return collars