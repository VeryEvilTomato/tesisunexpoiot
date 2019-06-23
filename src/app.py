import os
from flask import Flask, request, app
from flask_restful import Api

from server.handlers.usuario import Usuario
from server.handlers.monitores import Monitor
from server.handlers.monitores import MonitorDia
from server.handlers.monitorDato import MonitorDato
from server.handlers.webapp import index

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.secret_key = "unexpoIoTtesis"
api = Api(app)

# API
api.add_resource(Usuario, '/api/registrar')
api.add_resource(Monitor, '/api/monitores')
api.add_resource(MonitorDato, '/api/monitores/dato')
api.add_resource(MonitorDia, '/api/monitores/dia')

# WebApp
app.add_url_rule('/', 'index', index)
