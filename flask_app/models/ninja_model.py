from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL



class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name, dojo_id,) VALUES (%(first_name)s, %(last_name)s,%(dojo_id)s,NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)

        all_ninjas = []

        for row in result:
            all_ninjas.append(cls(row))
        return all_ninjas

    @classmethod
    def create_one_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) "
        query += "VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"

        return connectToMySQL(DATABASE).query_db(query, data)



    @classmethod
    def get_one_ninja(cls,data):

        query = "SELECT * FROM ninjas WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result[0])
        return cls(result[0])
        