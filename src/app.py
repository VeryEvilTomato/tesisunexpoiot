import os
from flask import Flask, request
from flask_restful import Api

from server.handlers.user.users import User

#Configuración básica del servidor
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.secret_key = "unexpoIoTtesis"
api = Api(app)

#Rutas para el servidor
api.add_resource(User, '/api/user/register')
#api.add_resource(Monitor, '/monitors/<int:id_usuario>')
#api.add_resource(MonitorDia, '/monitores/<int:id_monitor>/<int:fecha>')
#api.add_resource(MonitorDato, '/monitores/dato')