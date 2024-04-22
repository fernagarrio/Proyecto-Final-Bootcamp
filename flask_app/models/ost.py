from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
from datetime import datetime 

class Ost:

    def __init__(self, data):
        self.id = data['id']
        self.folio  = data['folio']
        self.id_cliente = data['id_cliente']
        self.nombre = data['nombre']
        self.fecha = data['fecha']
        self.equipo = data['equipo']
        self.teclado = data['teclado']
        self.scanner_laser  = data['scanner_laser']
        self.display = data['display']
        self.touchpad = data['touchpad']
        self.gatillo = data['gatillo']
        self.carcasa_frontal = data['carcasa_frontal']
        self.carcasa_trasera = data['carcasa_trasera']
        self.puerto_comunicacion  = data['puerto_comunicacion']
        self.cabezal = data['cabezal']
        self.platen_roller = data['platen_roller']
        self.sensores = data['sensores']
        self.comunicacion = data['comunicacion']
        self.limpieza  = data['limpieza']
        self.observaciones  = data['observaciones']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_ost(form):
        is_valid = True

        if form['folio'] == '':
            flash('folio no puede ser vacio', 'Clientes')
            is_valid = False
        
        return is_valid
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO Ost (folio,id_cliente,fecha ,equipo ,teclado ,scanner_laser,display,touchpad,gatillo,carcasa_frontal,"
        query += "carcasa_trasera,puerto_comunicacion ,cabezal ,platen_roller,sensores,comunicacion,limpieza ,observaciones"
        query += ") VALUES (%(folio)s, %(id_cliente)s, %(fecha)s, %(equipo)s, "
        query += "%(teclado)s, %(scanner_laser)s, %(display)s, %(touchpad)s, %(gatillo)s, %(carcasa_frontal)s, "
        query += "%(carcasa_trasera)s, %(puerto_comunicacion)s, %(cabezal)s, %(platen_roller)s, %(sensores)s, "
        query += "%(comunicacion)s, %(limpieza)s, %(observaciones)s)"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result
    
    @classmethod
    def get_all(cls,form):
        query = "SELECT * from ost JOIN clientes ON ost.id_cliente = clientes.id where id_cliente = %(clid)s"
        results = connectToMySQL('esquema_servicio_tecnico').query_db(query,form)
        Osts = []
        for ost in results:
            Osts.append(cls(ost)) 
        
        return Osts
    
    @classmethod
    def get_by_id(cls, form):
        
        query = "SELECT ost.id, ost.folio, ost.id_cliente, clientes.nombre, ost.fecha,ost.equipo, ost.teclado, ost.scanner_laser, "
        query +="ost.display, ost.touchpad, ost.gatillo, ost.carcasa_frontal, ost.carcasa_trasera, ost.puerto_comunicacion, "
        query +="ost.cabezal, ost.platen_roller, ost.sensores, ost.comunicacion, ost.limpieza, ost.observaciones, ost.created_at, ost.updated_at "
        query +="from ost JOIN clientes ON ost.id_cliente = clientes.id WHERE ost.id = %(id)s"

        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form) 
        
        Osts = cls(result[0])
        return Osts
    
    @classmethod
    def update(cls, form):
        
        query = "update Ost SET fecha=%(fecha)s, equipo=%(equipo)s,teclado=%(teclado)s, "
        query +="scanner_laser=%(scanner_laser)s, display=%(display)s,touchpad=%(touchpad)s, gatillo=%(gatillo)s,"
        query +="carcasa_frontal=%(carcasa_frontal)s,carcasa_trasera=%(carcasa_trasera)s,puerto_comunicacion=%(puerto_comunicacion)s,"
        query +="cabezal=%(cabezal)s,platen_roller=%(platen_roller)s,sensores=%(sensores)s,comunicacion=%(comunicacion)s,"
        query +="limpieza=%(limpieza)s,observaciones=%(observaciones)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result
    
    @classmethod
    def delete(cls, form):
        
        query = "DELETE FROM Ost WHERE id = %(id)s"
        result = connectToMySQL('esquema_servicio_tecnico').query_db(query, form)
        return result