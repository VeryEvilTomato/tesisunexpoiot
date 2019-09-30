#imports
import os
import json
import traceback
from flask import Flask, render_template
from flask_jwt import JWT
from server.security import authenticate, identity

from server.handlers.webapp import index

#Configuración del servidor
app = Flask(__name__, static_folder='client/build/static', template_folder='client/build')
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.secret_key = "unexpoIoTtesis"

app.config['MQTT_USERNAME'] = 'server'
app.config['MQTT_PASSWORD'] = 'unexpoiot'
app.config['MQTT_CLIENT_ID'] = "http-server"
app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authenticate, identity)

##Webapp
@app.route('/')
def serve():
    return render_template('index.html')