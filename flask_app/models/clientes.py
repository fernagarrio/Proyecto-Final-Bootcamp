from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
from datetime import datetime 


class Clientes:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.rut = data['rut']
        self.direccion= data['direccion']
        self.telefono= data['telefono']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_clientes(form):
        is_valid = True

        if form['rut'] == '':
            flash('rut no puede ser vacio', 'Clientes')
            is_valid = False
        
        if form['nombre'] == '':
            flash('nombre no puede ser vacio', 'Clientes')
            is_valid = False
               
        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO Clientes (nombre,rut,direccion,telefono) VALUES (%(nombre)s, %(rut)s, %(direccion)s, %(telefono)s)"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * from clientes"
        results = connectToMySQL('esquema_servicio_tecnico').query_db(query) 
        Clientes = []
        for cli in results:
            Clientes.append(cls(cli)) 
        
        return Clientes
    
    @classmethod
    def get_by_id(cls, form):
        
        query = "SELECT id,nombre,rut,direccion,telefono,created_at,updated_at from clientes WHERE Clientes.id = %(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form) 
        
        Clientes = cls(result[0])
        return Clientes
    
    @classmethod
    def update(cls, form):
        
        query = "update Clientes SET nombre=%(nombre)s, direccion=%(direccion)s, telefono=%(telefono)s,rut=%(rut)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, form):
        
        query = "DELETE FROM Clientes WHERE id = %(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result