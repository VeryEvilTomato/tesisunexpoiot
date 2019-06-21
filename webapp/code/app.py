import os
from flask import Flask, request
from flask_restful import Api

from resources.usuario import Usuario
from resources.monitores import Monitor
from resources.monitores import MonitorDia
from resources.monitorDato import MonitorDato

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = False
app.secret_key = "unexpoIoTtesis"
api = Api(app)

api.add_resource(Usuario, '/registrar')
api.add_resource(Monitor, '/monitores')
api.add_resource(MonitorDato, '/monitores/dato')
api.add_resource(MonitorDia, '/monitores/dia')

if __name__ == '__main__':
    from db import _db
    _db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def crear_tablas():
            _db.create_all()

    app.run(port=5000)