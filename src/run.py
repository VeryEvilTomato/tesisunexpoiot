from app import app
from mqtt.mqtt_client import MqttClient
from server.data.db import _db
from server.init_rest import init_rest

_db.init_app(app)
MqttClient.init_app(app)
init_rest(app)

@app.before_first_request
def create_tables():
    _db.create_all()

app.run(host='0.0.0.0',port=5000)