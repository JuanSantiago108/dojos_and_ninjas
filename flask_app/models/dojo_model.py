from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja


class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        


    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL(DATABASE).query_db( query, data)
    

    @classmethod
    def get_dojos_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas On ninjas.dojo_id = dojos.id WHERE dojos.id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        dojo = cls( results[0] )
        print(results)
        for row in results:
            ninja_data = {
                "id":row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "age":row['age'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo



    @classmethod
    def create_one_dojo(cls,data):
        query = "INSERT INTO dojos (name) "
        query += "VALUES(%(name)s);"

        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)

        all_dojos = []

        for row in result:
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod
    def get_one_dojo(cls,data):

        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return cls(result[0])


    @classmethod
    def edit_one_dojo(cls,data):
        query = "UPDATE dojos "
        query += "SET first_name =%(name)s;"
        return connectToMySQL(DATABASE).query_db( query, data )
    

    @classmethod
    def delete_one_user(cls,data):
        query = "DELETE FROM dojos "
        query += "WHERE id= %(id)s "
        return connectToMySQL(DATABASE).query_db( query, data )

