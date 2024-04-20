#pipenv install flask pymysql flask-bcrypt
#Importamos la app

from flask_app import app 

#Importamos controladores
from flask_app.controllers import users_controller ,clientes_controller, ost_controller

#Ejecución de app
if __name__ == "__main__":
    app.run(debug=True) #(debug=True, port=3400)