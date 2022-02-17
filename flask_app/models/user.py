from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

# from flask_app.models import message     



 #CREATE model
class User:
    db = 'user_to_friends'
    def __init__(self, data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
#CREATE model
    @classmethod
    def create_user(cls, data):
        query= '''
        Insert INTO users (first_name, last_name)
        VALUES (%(first_name)s, %(last_name)s)
        ;'''
        return connectToMySQL(cls.db).query_db(query,data)
        #fat model:
        #user_id = connectToMySQL(cls.db).query_db(query,data)
        #session['user_id] = user_id


#READ model
    @classmethod
    def get_all_users(cls):  
        query = """
        SELECT *
        FROM users
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in result:
            users.append(cls(row))
        return users

    @classmethod
    def get_user_by_id(cls, id):
        data= {'id': id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
        # message.Message.get_all_messages(id) could put in this return or in controller

   