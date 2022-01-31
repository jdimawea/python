from flask_app.config.mysqlconnection import connectToMySQL


class User: 
    def __init__(self, data):
        #data is a dictionary that holds the data from the DB
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for row in results:
            users.append(cls(row))

        return users

    @classmethod
    def save(cls, data):

        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL('users_schema').query_db(query,data)
        
        return result