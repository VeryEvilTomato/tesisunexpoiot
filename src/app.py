import os
from flask import Flask, request
from flask_restful import Api

from server.handlers.user.users import User
from server.handlers.monitor.monitors import Monitor
from server.handlers.monitor.data import MonitorDatum
from server.handlers.monitor.day import MonitorDay

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
api.add_resource(Monitor, '/api/user/<int:id_user>/monitors/<int:id_monitor>')
api.add_resource(MonitorDatum, '/api/user/<int:id_user>/monitors/<int:id_monitor>/data')
api.add_resource(MonitorDay, '/api/user/<int:id_user>/monitors/<int:id_monitor>/data/date/<string:date>')
