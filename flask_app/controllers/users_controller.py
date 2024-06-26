from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from datetime import datetime 

#Importamos TODOS los modelos
from flask_app.models.users import User
from flask_app.models.clientes import Clientes
from flask_app.models.ost import Ost

#Importamos BCrypt -> Encriptar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    #request.form = {"first_name": "Elena", "last_name": "De Troya"......}

    #Validar que la info sea correcta
    if not User.validate_user(request.form):
        return redirect("/")
    
    #Encriptamos la contra
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    #Generamos un diccionario con toda la info Y LA CONTRA encriptada
    form = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pass_encrypt
    }

    nuevo_id = User.save(form) #Recibiendo el ID del nuevo Usuario
    session['user_id'] = nuevo_id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Crear una instancia del usuario en base a la sesión
    form = {"id": session['user_id']}
    user = User.get_by_id(form)

    cli = Clientes.get_all()

    return render_template("dashboard.html",  clientes=cli,  user=user, now=datetime.now)

@app.route("/dashboardost/<int:clid>")
def dashboardost(clid):
    #Verificar que el usuario inició sesión
    if 'user_id' not in session:
        return redirect("/")
    
    #Crear una instancia del usuario en base a la sesión
    form = {"id": session['user_id']}
    user = User.get_by_id(form)

    form2 = {'clid':clid}

    ost = Ost.get_all(form2) 

    session['idcli'] = clid
    return render_template("dashboardost.html", ost=ost,  user=user, now=datetime.now, clid=clid)

@app.route("/login", methods=['POST'])
def login():
    #request.form = {"email": "elena@cd.com", "password": "Hola123"}
    #Verificamos que el email exista en BD
    user = User.get_by_email(request.form) #user = instancia User O False

    if not user:
        flash("E-mail no registrado", "login")
        return redirect("/")
    
    #Si user SI es instancia de User
    if not bcrypt.check_password_hash(user.password, request.form['password']): #contra encryptada, contra no encr
        flash("Password incorrecto", "login")
        return redirect("/")
    
    session['user_id'] = user.id #Guardo en sesión el ID del usuario
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")