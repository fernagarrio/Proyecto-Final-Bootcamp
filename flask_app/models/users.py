#Importar la conexión BD
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #flash es el encargado de mostrar mensajes/errores

import re #Importar las Expresiones Regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email


class User:

    def __init__(self, data):
        #data = {diccionario con toda la info que quiero para instancia}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, form):
        #form = {"first_name":"Elena", "last_name":"De Troya", "email":"elena@cd.com", "password":YA ENCRIPTADA}
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_loginreg').query_db(query, form) #EL id del registro que creamos
        return result
    
    @staticmethod
    def validate_user(form):
        #form = {diccionario con todos los names y valores que el usuario ingresó}
        is_valid = True #Formulario inocente, no tiene nada de malo aún

        #Validar que el nombre tenga al menos 2 caracteres
        if len(form["first_name"]) < 2:
            flash("Nombre debe tener al menos 2 caracteres", "register")
            is_valid = False
        
        if len(form["last_name"]) < 2:
            flash("Apellido debe tener al menos 2 caracteres", "register")
            is_valid = False
        
        #Que el correo tenga el patrón correcto -> Expresiones Regulares
        if not EMAIL_REGEX.match(form["email"]):
            flash("E-mail inválido", "register")
            is_valid = False
        
        #Validamos que el correo sea único
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        if len(results) >= 1:
            flash("E-mail registrado previamente", "register")
            is_valid = False
        
        #Validar que la contra tenga al menos 6 caract
        if len(form["password"]) < 6:
            flash("Contraseña debe tener al menos 6 caracteres", "register")
            is_valid = False
        
        if form["password"] != form["confirm"]:
            flash("Contraseñas no coinciden", "register")
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_by_email(cls, form):
        #form = {"email": "elena@cd.com", "password": "Hola123"}
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_servicio_tecnico').query_db(query, form) #LISTA
        if len(results) == 1:
            #Si existe el usuario, me regresa solo 1 reg. [0]
            user = cls(results[0])
            return user #Regreso la instancia del usuario con ese correo
        else:
            return False
    
    @classmethod
    def get_by_id(cls, form):
        #form = {"id": 1}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)#LISTA de diccionarios.. Que tiene solo 1 posición
        user = cls(result[0])
        return user
