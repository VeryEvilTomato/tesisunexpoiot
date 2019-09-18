import os
from flask import Flask, request, render_template
from flask_restful import Api

from server.handlers.user.users import User
from server.handlers.user.options import Options
from server.handlers.user.devices import Devices

from server.handlers.monitor.monitor_submit import MonitorSubmit
from server.handlers.monitor.monitor_delete import MonitorDelete
from server.handlers.monitor.monitors import Monitors
from server.handlers.monitor.data import MonitorDatum
from server.handlers.monitor.day import MonitorDay

from server.handlers.switch.switch import Switch
from server.handlers.switch.switch_submit import SwitchSubmit
from server.handlers.switch.switch_delete import SwitchDelete
from server.handlers.switch.switches import Switches
from server.handlers.switch.switch_state import SwitchState

from server.handlers.webapp import index

#Configuración básica del servidor
app = Flask(__name__, static_folder='client/build/static', template_folder='client/build')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server/data/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.secret_key = "unexpoIoTtesis"
api = Api(app)

#Rutas para el servidor

##API
#User data
api.add_resource(User, '/api/user/register')
api.add_resource(Options, '/api/user/<int:id_user>/options')
api.add_resource(Devices, '/api/user/<int:id_user>/devices')
#Monitors
api.add_resource(Monitors, '/api/user/<int:id_user>/monitors')
api.add_resource(MonitorSubmit, '/api/user/<int:id_user>/monitors')
api.add_resource(MonitorDelete, '/api/user/<int:id_user>/monitors/<int:id_monitor>')
api.add_resource(MonitorDatum, '/api/user/<int:id_user>/monitors/<int:id_monitor>/data')
api.add_resource(MonitorDay, '/api/user/<int:id_user>/monitors/<int:id_monitor>/data/date/<string:date>')
#Switches
api.add_resource(Switch, '/api/user/<int:id_user>/switches/<int:id_switch>')
api.add_resource(Switches, '/api/user/<int:id_user>/switches')
api.add_resource(SwitchSubmit, '/api/user/<int:id_user>/switches')
api.add_resource(SwitchDelete, '/api/user/<int:id_user>/switches/<int:id_switch>')
api.add_resource(SwitchState, '/api/user/<int:id_user>/switches/<int:id_switch>')

##Webapp
@app.route('/')
def serve():
    return render_template('index.html')