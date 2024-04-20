from flask import Flask #Importamos Flask

app = Flask(__name__) #Inicializamos app

app.secret_key = "Llave que te importa" #Se necesita para la sesión